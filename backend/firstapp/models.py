from django.db import models

from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=500)
    img = models.CharField(null=True, blank=True, max_length=250)
    content = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    createtime = models.DateField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=500)
    avatar = models.CharField(max_length=250, default="static/images/default.png")
    comment = models.TextField(null=True, blank=True)
    createtime = models.DateField(auto_now=True)

    belong_to = models.ForeignKey(to=Article, related_name="under_comments", null=True, blank=True)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    voter = models.ForeignKey(to=User, related_name="user_tickets")
    article = models.ForeignKey(to=Article, related_name="article_tickets")

    ARTICLE_CHOICES = {
        ("like", "like"),
        ("dislike", "dislike"),
        ("normal", "normal")
    }
    choice = models.CharField(choices=ARTICLE_CHOICES, max_length=10)

    def __str__(self):
        return str(self.id)


class UserProfile(models.Model):
    name = models.CharField(null=True, blank=True, help_text='你的真实姓名', max_length=20)
    SEX_CHOICES = (
        ('性别', '性别'),
        ('男', '男'),
        ('女', '女'),
    )
    sex = models.CharField(null=True, blank=True, max_length=10, choices=SEX_CHOICES)
    password = models.CharField(null=True, blank=True, max_length=20)
    avatar = models.FileField(upload_to='avatar_image', null=True)

    belong_to = models.OneToOneField(to=User, related_name='profile', null=True, blank=True)

    def __str__(self):
        return self.name


# class Collection(models.Model):
#     user_collection = models.ForeignKey(to=User, related_name='user_collection', null=True, blank=True)
#
#     article_collection = models.ForeignKey(to=Article, related_name='article_collection', null=True, blank=True)
#
#     def __str__(self):
#         return self
