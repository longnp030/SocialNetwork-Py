from post.models import Comment, Post, Reaction
from notification.models import PostNotification
import json
import datetime as dt

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

class PostConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.me = self.scope['user']
        print(self.me)
        self.room_name = self.scope['url_route']['kwargs']['post_id']
        self.room_group_name = 'comment_%s' % self.room_name
        print(self.room_name)
        print(self.room_group_name)
        print(self.channel_name)
        print(self.channel_layer)

        # Get post database to save comment
        self.post = await database_sync_to_async(
            Post.objects.get)(id=self.room_name)

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

    # Receive comment from WebSocket
    # This is what received when user click enter to post a comment on page
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        try:
            comment = text_data_json['comment']
            print(comment)

            # Save comments to database
            comment_obj = Comment(
                commentor=self.me,
                post=self.post,
                content=comment,
                written=dt.datetime.now,
                modified=dt.datetime.now
            )
            await database_sync_to_async(comment_obj.save)()

            notification_obj = PostNotification(
                actor=self.me,
                action='commented on',
                recipient=self.post.author,
                post=self.post,
                notified=dt.datetime.now,
            )
            await database_sync_to_async(notification_obj.save)()
               
            # Send comment to room group
            # These are what will be sent to the post_comment function below
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'post_comment',
                    'comment': comment,
                    'commentor_id': comment_obj.commentor.id,
                    'commentor_name': comment_obj.commentor.username,
                    'post_author_id': self.post.author.id,
                    'notification': notification_obj.actor.username + " commented on your post at " + str(notification_obj.notified),
                    'target': 'comment',
                }
            )
        except Exception:
            reaction = text_data_json['reaction']
            if reaction == "liked":
                reaction_obj = Reaction(post=self.post, liker=self.me)
                await database_sync_to_async(reaction_obj.save)()
                '''reaction_count = await self.get_reaction_count()'''

                notification_obj = PostNotification(
                    actor=reaction_obj.liker,
                    action='liked',
                    recipient=self.post.author,
                    post=self.post,
                    notified=dt.datetime.now,
                )
                await database_sync_to_async(notification_obj.save)()

                # Send comment to room group
                # These are what will be sent to the post_comment function below
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'post_reaction',
                        'liker_id': reaction_obj.liker.id,
                        'liker_name': reaction_obj.liker.username,
                        'target': 'reaction',
                        #'reaction_count': reaction_count,
                        'post_author_id': self.post.author.id,
                        'notification': notification_obj.actor.username + " liked your post on " + str(notification_obj.notified),
                        'reaction': reaction,
                    }
                )
            else:
                reaction_obj = await database_sync_to_async(Reaction.objects.get)(post=self.post, liker=self.me)
                '''reaction_count = await self.get_reaction_count()
                print(reaction_count)'''

                notification_obj = await database_sync_to_async(PostNotification.objects.get)(
                    actor=reaction_obj.liker,
                    action='liked',
                    post=reaction_obj.post,
                )

                await database_sync_to_async(reaction_obj.delete)()
                await database_sync_to_async(notification_obj.delete)()

                # Send comment to room group
                # These are what will be sent to the post_comment function below
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'post_reaction',
                        'unliker_id': self.me.id,
                        'unliker_name': self.me.username,
                        'target': 'reaction',
                        #'reaction_count': reaction_count,
                        'reaction': reaction,
                    }
                )

    @database_sync_to_async
    def get_reaction_count(self):
        return Reaction.objects.filter(post=self.post).count()
    
    # Receive comment from room group
    async def post_comment(self, event):
        comment = event['comment']
        commentor_id = event['commentor_id']
        commentor_name = event['commentor_name']
        post_author_id = event['post_author_id']
        notification = event['notification']
        target = event['target']

        # Send comment to WebSocket
        # These are what HTML file will receive
        await self.send(text_data=json.dumps({
            'comment': comment,
            'commentor_id': commentor_id,
            'commentor_name': commentor_name,
            'post_author_id': post_author_id,
            'notification': notification,
            'target': target,
        }))

    # Receive comment from room group
    async def post_reaction(self, event):
        target = event['target']
        #reaction_count = event['reaction_count']
        if event['reaction'] == 'liked':
            liker_id = event['liker_id']
            liker_name = event['liker_name']
            post_author_id = event['post_author_id']
            notification = event['notification']
            reaction = event['reaction']

            # Send comment to WebSocket
            # These are what HTML file will receive
            await self.send(text_data=json.dumps({
                'liker_id': liker_id,
                'liker_name': liker_name,
                #'reaction_count': reaction_count,
                'post_author_id': post_author_id,
                'notification': notification,
                'target': target,
                'reaction': reaction
            }))
        else:
            unliker_id = event['unliker_id']
            unliker_name = event['unliker_name']
            reaction = event['reaction']

            # Send comment to WebSocket
            # These are what HTML file will receive
            await self.send(text_data=json.dumps({
                'unliker_id': unliker_id,
                'unliker_name': unliker_name,
                #'reaction_count': reaction_count,
                'target': target,
                'reaction': reaction
            }))
