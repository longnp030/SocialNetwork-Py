import json
import datetime as dt

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class HomeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.me = self.scope['user']
        print(self.me.is_online)

        self.room_group_name = 'home'

        # Assign online status to me when I connect to socket
        self.me.is_online = True
        self.me.save()

        print(self.me.is_online)

        # Join group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        # Assign offline status to me when I disconnect
        self.me.is_online = False
        self.me.save()
        print(self.me.is_online)

        # Leave group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive comment from WebSocket, when user interact with page
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        status = text_data_json['status']
        print(status)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'update_status',
                'status': status,
                'username': self.me.username,
                'user_id': self.me.id,
            }
        )
    
    async def update_status(self, event):
        status = event['status']
        username = event['username']
        user_id = event['user_id']

        # Send comment to WebSocket
        # These are what HTML file will receive
        await self.send(text_data=json.dumps({
            'status': status,
            'username': username,
            'user_id': user_id,
        }))
