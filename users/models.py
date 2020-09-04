from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=80)
    image = models.ImageField(default='fam.jpg', upload_to='media')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return "{}".format(self.user)
      
    
   




@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)




@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
     
    