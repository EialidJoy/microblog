from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# from django.urls import reverse

# Create your models here.
class Post(models.Model):
	description=models.TextField(null=True)
	user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)


class Comment(models.Model):
	comment_description=models.TextField(null=True)
	post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    
	# def get_absolute_url(self):
	# 	return reverse("comment",kwargs={"id":self.id})