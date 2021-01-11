from django.db import models
from business.models import User
from PIL import Image
from django.utils import timezone
from django.urls import reverse

class Blog(models.Model):
    the_photo = models.ImageField(upload_to='blog_pics')
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)#set's the time the post was posted
    author = models.ForeignKey(User, on_delete=models.CASCADE)#ON DELETE meaning if a user is deleted so does the posts of the user
    #likes = models.ManyToManyField(User, related_name='blogpost_like')

    #def number_of_likes(self):
    #    return self.likes.count()
    def __str__(self):
        return self.title
    def get_pk(self):
        p_k = {"pk" : self.pk}
        return p_k
    def get_absolute_url(self):
        p_k = self.get_pk()
        return reverse('blog')
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.the_photo.path)
        if img.height > 300 and img.width > 300:
            output_size = (1024, 764)
            img.thumbnail(output_size)
            img.save(self.the_photo.path)


class BlogComment(models.Model):
    code = models.IntegerField()
    message = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.message

class AllBlogComment(models.Model):
    code = models.IntegerField()
    message = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.message
        
    

