from django.db import models

class User(models.Model):
    ID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length = 100)
    Email = models.EmailField(max_length = 100)
    Passowrd = models.CharField(max_length = 100)

class Post(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length = 100)
    Content = models.TextField()
    Category = models.CharField(max_length = 100)
    DatePublished = models.DateField()

class Comment(models.Model):
    ID = models.AutoField(primary_key=True)
    PostID = models.ForeignKey(Post, on_delete = models.CASCADE)
    UserID = models.ForeignKey(User, on_delete = models.CASCADE)
    Content = models.TextField()
    DatePosted = models.DateField()

class Category(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length = 100)