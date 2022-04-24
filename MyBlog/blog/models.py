from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.urls import clear_script_prefix, reverse
# Create your models here.

# For Post Created By User
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def approve_comment(self):
        return self.comments.filter(approved_comment=True)
    
# For Comments Done by Any Person
class Comments(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
        
    def get_absolute_url(self):
        return reverse("post_list")
        
    def __str__(self):
        return self.text
    
    