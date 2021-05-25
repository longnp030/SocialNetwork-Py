from django import db
from django.db import models
from user.models import User
from post.models import Post

# Create your models here.

def image_upload_location(instance, filename):
    return 'post/images/g%s-%s.%s' % (instance.id, instance.name, filename.split('.')[1])

class Group(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    cover_image = models.ImageField(max_length=255, upload_to=image_upload_location, db_column='cover_image')
    name = models.CharField(max_length=255, verbose_name='group_name', db_column='name')
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="group_creator",
        related_name='group_creator',
        db_column='creator'
    )
    admins = models.ManyToManyField(
        User,
        verbose_name="group_admins",
        related_name='group_admins',
        db_column='admins',
        through='GroupAdmin'
    )
    PRIVACY = (
        ('Public', 'public'),
        ('Private', 'private'),
    )
    privacy = models.CharField(
        verbose_name='group_privacy',
        choices=PRIVACY,
        default='Public',
        max_length=100,
        db_column='privacy'
    )
    description = models.CharField(
        max_length=1000,
        verbose_name="group_description",
        db_column='description'
    )
    CATEGORY = (
        ('General', 'general'),
        ('Entertainment', 'entertainment'),
        ('Education', 'education'),
        ('Sport', 'sport'),
        ('Travel', 'travel'),
        ('Business', 'business'),
        ('Animal', 'animal'),
        ('Health', 'health'),
        ('Life', 'life'),
        ('Commerce', 'commerce'),
    )
    category = models.CharField(
        verbose_name='category',
        choices=CATEGORY,
        default='General',
        max_length=100,
        db_column='category'
    )
    members = models.ManyToManyField(
        User,
        verbose_name='group_members',
        related_name='group_members',
        db_column='members',
        through='GroupMember'
    )
    posts = models.ManyToManyField(
        Post,
        verbose_name='group_posts',
        related_name='group_posts',
        db_column='posts',
        through='GroupPost'
    )
    created = models.DateTimeField(auto_now_add=True, db_column='created')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'group'
        managed = False

class GroupAdmin(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, db_column='admin')
    was = models.DateTimeField(auto_now_add=True, db_column='was')
    
    def __str__(self):
        return str(self.group.id) + '-' + self.group.name + '-' + str(self.admin.id) + '-' + self.admin.username
    
    class Meta:
        db_table = 'group_admin'
        managed = False

class GroupMember(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group')
    member = models.ForeignKey(User, on_delete=models.CASCADE, db_column='member')
    was = models.DateTimeField(auto_now_add=True, db_column='was')

    def __str__(self):
        return str(self.group.id) + '-' + self.group.name + '-' + str(self.member.id) + '-' + self.member.username

    class Meta:
        db_table = 'group_member'
        managed = False

class GroupPost(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, db_column='post')

    def __str__(self):
        return str(self.group.id) + '-' + self.group.name + '-' + str(self.post.id) + '-' + self.post.text

    class Meta:
        db_table = 'group_post'
        managed = False

class JoinGroupRequest(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='group_join_request',
        db_column='group'
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='group_join_request_sender',
        db_column='sender'
    )
    sent = models.DateTimeField(auto_now_add=True, db_column='sent')

    class Meta:
        db_table = 'joingrouprequest'
        managed = False
    
    def __str__(self):
        return self.group.name + '-' + self.sender.username

class GroupJoinInvitation(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='group_invited_to',
        db_column='group'
    )
    inviter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='group_join_inviter',
        db_column='inviter'
    )
    invitee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='group_join_invitee',
        db_column='invitee'
    )
    invited = models.DateTimeField(auto_now_add=True, db_column='invited')

    class Meta:
        db_table = 'groupjoininvitation'
        managed = False
