from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    title_tag = models.CharField(max_length=100, default='Spottiapp')
    post_date = models.TimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')


    def total_likes(self):
        return self.likes.count()



    def __str__(self):
        return self.title + ' | ' + str(self.author)
    


    def get_absolute_url(self):
        return reverse('article-detail', args=(self.id,))




class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    time_added = models.TimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
