from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    user_name = models.CharField(max_length = 20)
    profile_pic = models.TextField()

    def __str__(self):
        return f"{self.user_name}"
    
class Subs(models.Model):
    title = models.CharField(max_length = 20)
    followers = ArrayField(models.IntegerField())
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        # related_name='readme'
    )
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"
    
class Post(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    img_url = models.TextField()
    up_votes = models.IntegerField()
    down_votes = models.IntegerField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        # related_name='readme'
    )
    sub = models.ForeignKey(
        Subs,
        on_delete=models.CASCADE,
        # related_name='readme'
    )

    def __str__(self):
        return f"{self.title}"

class Comments(models.Model):
    comment =  models.TextField(max_length = 500)
    commenter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        # related_name='readme'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        # related_name='readme'
    )
    up_votes = models.IntegerField()
    down_votes = models.IntegerField()

    def __str__(self):
        return f"{self.comment}"

