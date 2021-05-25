from django.db import models
import datetime as dt

from user.models import *

# Create your models here.

class ChatBox(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    user1 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='chat_user1',
        verbose_name='chat_user1',
        db_column='user1',
    )
    user2 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='chat_user2',
        verbose_name='chat_user2',
        db_column='user2',
    )
    created = models.DateTimeField(auto_now_add=True, db_column='created')
    name = models.CharField(
        max_length=45,
        verbose_name='name',
        db_column='name')

    def save(self, *args, **kwargs):
        #self.name = self.user1.username + '-' + self.user2.username
        if not self.name:
            self.name = str(self.user1.id+self.user2.id)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.user1.username + '-' + self.user2.username)

    class Meta:
        db_table = 'chatbox'
        managed = False

class Message(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='chat_sender',
        verbose_name='chat_sender',
        db_column='sender',
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='chat_receiver',
        verbose_name='chat_receiver',
        db_column='receiver',
    )
    content = models.TextField(verbose_name='content', db_column='content')
    chatbox = models.ForeignKey(
        ChatBox,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name='chatbox',
        db_column='chatbox',
    )
    sent = models.DateTimeField(auto_now_add=True, db_column='sent')

    def __str__(self):
        return '(' + self.sender.username + '-' + self.receiver.username + ') ' + self.content
    
    class Meta:
        db_table = 'message'
        managed = False


class GroupChatBox(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='chat_creator',
        verbose_name='chat_creator',
        db_column='creator',
    )
    created = models.DateTimeField(auto_now_add=True, db_column='created')
    name = models.CharField(
        max_length=45,
        verbose_name='name',
        db_column='name')

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = str(self.creator.id) + '-' + str(dt.datetime.now())
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'groupchatbox'
        managed = False

class JoinGroupChat(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    groupchatbox = models.ForeignKey(
        GroupChatBox,
        related_name='groupchatbox',
        verbose_name='groupchat',
        on_delete=models.CASCADE,
        db_column='groupchatbox',
    )
    inviter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='inviter',
        related_name='invite_user',
        db_column='inviter',
    )
    invitee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='invited_user',
        verbose_name='inivitee',
        db_column='invitee',
    )
    joined = models.DateTimeField(auto_now_add=True, db_column='joined')

    def __str__(self):
        return self.inviter.username + '-' + self.invitee.username
    
    class Meta:
        db_table = 'joingroupchat'
        unique_together = ['groupchatbox', 'invitee']
        managed = False

class GroupMessage(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='groupchat_sender',
        verbose_name='groupchat_sender',
        db_column='sender',
    )
    content = models.TextField(verbose_name='content', db_column='content')
    chatbox = models.ForeignKey(
        GroupChatBox,
        on_delete=models.CASCADE,
        related_name='groupmessages',
        verbose_name='groupchatbox',
        db_column='chatbox',
    )
    sent = models.DateTimeField(auto_now_add=True, db_column='sent')

    def __str__(self):
        return self.sender.username + '-' + self.content
    
    class Meta:
        db_table = 'groupmessage'
        managed = False
