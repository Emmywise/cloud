from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    location = models.CharField(max_length=30, blank=True)
    #portfolio_site = models.URLField(blank=True)
    # profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
        
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.description

    def delete(self, *args, **kwargs):
        self.document.delete()
        super().delete(*args, **kwargs)

class ImageUpload(models.Model):
    caption = models.CharField(max_length=21, blank=True)
    image = models.ImageField(upload_to ='images/%y%m%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    #user = models.ForeignKey(User, on_delete=CASCADE)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)