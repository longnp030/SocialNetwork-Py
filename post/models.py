from django.db import models
from user.models import *

# Create your models here.

def image_upload_location(instance, filename):
    return 'post/images/p%s-%s.%s' % (instance.id, instance.author.username, filename.split('.')[1])


class Image(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_column='author')
    image = models.ImageField(max_length=255, upload_to=image_upload_location, db_column='image', null=True)
    uploaded = models.DateTimeField(auto_now_add=True, db_column='uploaded')

    def __str__(self):
        if self.image:
            return self.image.url[13:]
        else:
            return str(self.id)
    
    class Meta:
        db_table = 'image'
        managed = False


class Post(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    author = models.ForeignKey(
        User,
        related_name='creator', verbose_name='author',
        on_delete=models.CASCADE,
        db_column='author'
    )
    receiver = models.ForeignKey(
        User,
        related_name='post_receiver', verbose_name='post_receiver',
        on_delete=models.CASCADE,
        db_column='receiver',
        blank=True
    )
    tagged_friends = models.ManyToManyField(
        to=User,
        verbose_name='tagged_friends',
        db_column='tagged_friends',
        through='FriendTaggedInPost',
        blank=True,
        null=True
    )
    text = models.TextField(blank=True, null=True, db_column='text')
    images = models.ManyToManyField(
        to=Image,
        verbose_name='images',
        db_column='images',
        through='PostImage'
    )
    group = models.ForeignKey(
        'group.Group',
        on_delete=models.CASCADE,
        related_name='group_belongto',
        null=True,
        blank=True,
        db_column='group'
    )

    topic = models.CharField(
        verbose_name='topic',
        max_length=20,
        db_column='topic')

    created = models.DateTimeField(auto_now_add=True, db_column='created')
    modified = models.DateTimeField(auto_now=True, db_column='modified')

    def __str__(self):
        return self.author.username + '-' + self.text

    class Meta:
        db_table = 'post'
        managed = False
    
class FriendTaggedInPost(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, db_column='post')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, db_column='friend')
    tagged_at = models.DateTimeField(auto_now_add=True, db_column='tagged')

    def __str__(self):
        return self.post.author.username + '-' + self.text + '-' + self.friend.username

    class Meta:
        db_table = 'friendtaggedinpost'
        managed = False

class PostImage(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, db_column='post_id')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, db_column='image_id')

    def __str__(self):
        return str(self.post.id) + '-' + str(self.image.id)
    
    class Meta:
        db_table = 'post_images'
        managed = False

class Reaction(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    post = models.ForeignKey(
        Post,
        related_name='reaction', verbose_name="post",
        db_column='post',
        on_delete=models.CASCADE,
    )
    liker = models.ForeignKey(
        User,
        related_name='liker',
        db_column='liker',
        on_delete=models.CASCADE,
    )
    '''love = models.IntegerField(
        verbose_name='love', blank=True, null=True,
        db_column='love'
    )
    care = models.IntegerField(
        verbose_name='care', blank=True, null=True,
        db_column='care'
    )
    haha = models.IntegerField(
        verbose_name='haha', blank=True, null=True,
        db_column='haha'
    )
    sad = models.IntegerField(
        verbose_name='sad', blank=True, null=True,
        db_column='sad'
    )
    angry = models.IntegerField(
        verbose_name='angry', blank=True, null=True,
        db_column='angry'
    )'''
    def __str__(self):
        return self.post.author.username + '-' + self.post.text + '-' + self.liker.username

    class Meta:
        db_table = 'reaction'
        managed = False


class Comment(models.Model):
    id = models.AutoField(primary_key=True, unique=True, db_column='id')
    commentor = models.ForeignKey(
        User,
        verbose_name='commentor',
        on_delete=models.CASCADE,
        db_column='commentor'
    )
    post = models.ForeignKey(
        Post,
        verbose_name='post commented on',
        on_delete=models.CASCADE,
        db_column='post',
    )
    content = models.CharField(
        verbose_name='comment',
        max_length=1000,
        blank=True, null=True,
        db_column='content',
    )
    written = models.DateTimeField(auto_now_add=True, db_column='written')
    modified = models.DateTimeField(auto_now=True, db_column='modified')

    def __str__(self):
        return str(self.post.id) + '-' + self.commentor.username + '-' + self.content

    class Meta:
        db_table = 'comment'
        managed = False
