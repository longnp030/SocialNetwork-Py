from django.contrib.contenttypes.models import *
from django.contrib.contenttypes.fields import *
from django.db import models

from user.models import *
from post.models import *

# Create your models here.

'''class Notification(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    from_obj_content_type = models.ForeignKey(
        ContentType,
        related_name='notify_from',
        on_delete=models.CASCADE,
        db_column='from_obj_content_type',
    )
    from_obj_id = models.PositiveIntegerField(db_column='from_obj_id',)
    from_obj = GenericForeignKey('from_obj_content_type', 'from_obj_id')

    to_obj_content_type = models.ForeignKey(
        ContentType,
        related_name='notify_to',
        on_delete=models.CASCADE,
        db_column='to_obj_content_type',
    )
    to_obj_id = models.PositiveIntegerField(db_column='to_obj_id',)
    to_obj = GenericForeignKey('to_obj_content_type', 'to_obj_id')

    action = models.CharField(max_length=1000, db_column='action',)
    
    action_obj_content_type = models.ForeignKey(
        ContentType,
        related_name='notify_of',
        on_delete=models.CASCADE,
        db_column='action_obj_content_type'
    )
    action_obj_id = models.PositiveIntegerField(db_column='action_obj_id')
    action_obj = GenericForeignKey('action_obj_content_type', 'action_obj_id')

    notified = models.DateTimeField(auto_now_add=True, db_column='notified')

    def __str__(self):
        context = {
            'from': self.from_obj,
            'action': self.action,
            'action_object': self.action_obj,
            'to': self.to_obj,
            'when': self.notified
        }
        if self.to_obj:
            if self.action_obj:
                return u'%(from)s %(action)s %(action_object)s on %(to)s at %(when)s' % context
            return u'%(from)s %(action)s %(to)s at %(when)s' % context
        if self.action_obj:
            return u'%(from)s %(action)s %(action_object)s at %(when)s' % context
        return u'%(from)s %(action)s at %(when)s' % context'''


class PostNotification(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    actor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notify_from',
        db_column='actor',
    )
    action = models.CharField(max_length=1000, db_column='action')
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notify_to',
        db_column='recipient',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='notify_of',
        db_column='post',
    )
    notified = models.DateTimeField(auto_now_add=True, db_column='notified')

    def __str__(self):
        context = {
            'actor': self.actor,
            'action': self.action,
            'recipient': self.recipient,
            'post': self.post,
            'notified': self.notified,
        }
        return u"%(actor)s %(action)s %(recipient)s's %(post)s on %(notified)s." % context

    class Meta:
        db_table = 'postnotification'
        managed = False
    