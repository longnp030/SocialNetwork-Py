# chat/consumers.py
from django.db.models.query_utils import Q
from chat.models import *
import json
import datetime as dt

from channels.db import database_sync_to_async
from user.models import User
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.me = self.scope['user']
        self.friend = await database_sync_to_async(
            User.objects.get
        )(id=self.scope['url_route']['kwargs']['user_id'])  # get(id=self.scope['url_route']['kwargs']['user_id'])
        print(self.me)
        print(self.friend)
        self.room_name = await self.get_room_name()
        self.room_group_name = 'chat_%s' % self.room_name
        print(self.room_name)
        print(self.room_group_name)
        print(self.channel_name)
        print(self.channel_layer)

        # Get database box to save chat status
        self.chatbox = await database_sync_to_async(
            ChatBox.objects.get)(name=self.room_name)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    @database_sync_to_async
    def get_room_name(self):
        return ChatBox.objects.get(
                (Q(user1=self.me)|Q(user2=self.me))&(Q(user1=self.friend)|Q(user2=self.friend))
            ).name

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    # This is what received when user click enter to send message on page
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json['message']
        print(message)

        # Save messages to database
        message_obj = Message(
            sender=self.me, receiver=self.friend,
            content=message,
            chatbox=self.chatbox,
            sent=dt.datetime.now
        )
        await database_sync_to_async(message_obj.save)()

        # Send message to room group
        # These are what will be sent to the chat_message function below
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_name': message_obj.sender.username,
                'sender_id': message_obj.sender.id,
                'sender_avt': message_obj.sender.avatar.url,
                'receiver': message_obj.receiver.username,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender_name = event['sender_name']
        sender_id = event['sender_id']
        sender_avt = event['sender_avt']
        receiver = event['receiver']

        # Send message to WebSocket
        # These are what HTML file will receive
        await self.send(text_data=json.dumps({
            'message': message,
            'sender_name': sender_name,
            'sender_id': sender_id,
            'sender_avt': str(sender_avt),
            'receiver': receiver,
        }))


class GroupChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.me = self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['group_chat_id']
        self.room_group_name = 'group_chat_%s' % self.room_name
        print(self.room_name)
        print(self.room_group_name)
        print(self.channel_name)
        print(self.channel_layer)

        # Get database box to save chat status
        self.chatbox = await database_sync_to_async(
            GroupChatBox.objects.get)(id=self.room_name)
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    # This is what received when user click enter to send message on page
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json['message']
            
        try:
            member_id = text_data_json['member_id']
        except:
            member_id = None
        if member_id:
            member = await database_sync_to_async(User.objects.get)(id=int(member_id))
            valid_join = await database_sync_to_async(JoinGroupChat.objects.filter)(groupchatbox=self.chatbox, invitee=member)
            if len(valid_join) > 0:
                print(len(valid_join))
                return
            else:
                message = "added " + member.username + " to this chat."

        try:
            kick_member_id = text_data_json['kick_member_id']
        except:
            kick_member_id = None;
        if kick_member_id:
            member = await database_sync_to_async(User.objects.get)(id=int(kick_member_id))
            message = "removed " + member.username + " from this chat."

        try:
            leave_member_id = text_data_json['leave_member_id']
        except:
            leave_member_id = None
        if leave_member_id:
            member = await database_sync_to_async(User.objects.get)(id=int(leave_member_id))
            if member == self.chatbox.creator:
                second_joined_member = await database_sync_to_async(JoinGroupChat.objects.order_by)('joined')
                second_joined_member = second_joined_member[0].invitee
                self.chatbox.creator = second_joined_member
                await database_sync_to_async(self.chatbox.save)()
                message = member.username + " left this chat. Admin right is transferred to " + self.chatbox.creator.username

                await database_sync_to_async(JoinGroupChat.objects.get(invitee=self.chatbox.creator).delete)()
                for join in await database_sync_to_async(JoinGroupChat.objects.all)():
                    join.inviter = self.chatbox.creator
            else:
                message = member.username + " left this chat."

            print(message)
            message_obj = GroupMessage(
                sender=self.chatbox.creator,
                content=message,
                chatbox=self.chatbox,
                sent=dt.datetime.now
            )
            await database_sync_to_async(message_obj.save)()

            # Send message to room group
            # These are what will be sent to the chat_message function below
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'sender': message_obj.sender.username,
                    'sent_at': str(message_obj.sent),
                    'groupchatbox': message_obj.chatbox.name,
                }
            )
            return

        try:
            new_chat_name = text_data_json['new_chat_name']
        except:
            new_chat_name = None
        if new_chat_name and len(new_chat_name) > 0:
            self.chatbox.name = new_chat_name
            await database_sync_to_async(self.chatbox.save)()
            print(self.chatbox.name)

        # Save messages to database
        print(message)
        print(new_chat_name)
        message_obj = GroupMessage(
            sender=self.me,
            content=message,
            chatbox=self.chatbox,
            sent=dt.datetime.now
        )
        await database_sync_to_async(message_obj.save)()

        # Send message to room group
        # These are what will be sent to the chat_message function below
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': message_obj.sender.username,
                'sent_at': str(message_obj.sent)[:-6],
                'groupchatbox': message_obj.chatbox.name,
                'new_chat_name': new_chat_name,
                'kick_member_id': kick_member_id,
            }
        )
    
    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        sent_at = event['sent_at']
        groupchatbox = event['groupchatbox']
        new_chat_name = event['new_chat_name']
        kick_member_id = event['kick_member_id']

        # Send message to WebSocket
        # These are what HTML file will receive
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'sent_at': sent_at,
            'groupchatbox': groupchatbox,
            'new_chat_name': new_chat_name,
            'kick_member_id': kick_member_id,
        }))


class ChatbotComsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.me = self.scope['user']
        self.bot = await database_sync_to_async(User.objects.get)(id=1)
        
        self.room_name = await self.get_room_name()
        self.room_group_name = 'chat_%s' % self.room_name
        print(self.room_name)
        print(self.room_group_name)
        print(self.channel_name)
        print(self.channel_layer)

        # Get database box to save chat status
        self.chatbox = await database_sync_to_async(
            ChatBox.objects.get)(name=self.room_name)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    @database_sync_to_async
    def get_room_name(self):
        return ChatBox.objects.get(
                (Q(user1=self.me)|Q(user2=self.me))&(Q(user1=self.bot)|Q(user2=self.bot))
            ).name

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    # This is what received when user click enter to send message on page
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json['message']
        print(message)

        # Save messages to database
        message_obj = Message(
            sender=self.me, receiver=self.bot,
            content=message,
            chatbox=self.chatbox,
            sent=dt.datetime.now
        )
        # await database_sync_to_async(message_obj.save)() !TODO

        ### This is where to generate bot's reply !TODO
        # id, reply = model.predict(message).get(id, reply)

        ### Save bot reply to database !TODO

        # Send message to room group
        # These are what will be sent to the chat_message function below
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_name': message_obj.sender.username,
                'sender_id': message_obj.sender.id,
                'sender_avt': message_obj.sender.avatar.url,
                'receiver': "LongBot",
                'bot_avt': message_obj.receiver.avatar.url,
                'reply': "Hello" if "hi" in message else "hom nay thu 7" if "thu may" in message else "toi ko hieu ban noi gi",
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender_name = event['sender_name']
        sender_id = event['sender_id']
        sender_avt = event['sender_avt']
        receiver = event['receiver']
        bot_avt = event['bot_avt']
        reply = event['reply']

        # Send message to WebSocket
        # These are what HTML file will receive
        await self.send(text_data=json.dumps({
            'message': message,
            'sender_name': sender_name,
            'sender_id': sender_id,
            'sender_avt': str(sender_avt),
            'receiver': receiver,
            'bot_avt': bot_avt,
            'reply': reply
        }))
