from django.db import models

# Create your models here.
from django.dispatch import receiver


from django.db.models.signals import post_save


from django.contrib.auth.models import User






class CustomUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self):
        return "User -> " + self.user.username
    

#this method is to create CustomUser when User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)

#this method to update profile when user is updated
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.customuser.save()




class Items(models.Model):
    price = models.FloatField(default = 0)
