from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

def validate_image_dimensions(image):

        img = Image.open(image)
        width, height = img.size

        if width <= 1000 or height <= 1000:
            raise ValidationError(f"Image width or height must be at least 1000px. Uploaded image width is {width}px and height is {height}px")


# Create your models here.


class PageBase(models.Model):
    title = models.CharField(max_length=200)
    sub_title  = models.CharField(max_length=250 , null=True, blank=True)
    bg_image = models.ImageField(upload_to='images/', null=True, blank=True , validators=[validate_image_dimensions])   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        abstract = True
        
    def __str__(self):
        return self.title
    


class HomePage(PageBase):
    pass

class AboutPage(PageBase):
    description = models.TextField()

class ContactPage(PageBase):
    description = models.TextField()
    
class Post(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = ('DR','Draft')
        PUBLISHED = ('PB', 'Published')
    
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    auther = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    bg_image=models.ImageField(upload_to='images/background_images')
    post_image=models.ImageField(upload_to='images/post_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    
    class Meta:
        ordering =['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("blog_post",args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug,
            ])
        
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    body = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    
    class Meta:
        ordering =['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]
    
    def __str__(self):
        return f"comment by {self.name} on post {self.post}"
    
    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    body = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    phone=models.CharField(max_length=15)
    
    class Meta:
        ordering =['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]
    
    def __str__(self):
        return f' send by {self.name}'
    


