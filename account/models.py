from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# in this case the profile is created using  a signal though it aint mandatory
# due to 121 field profile is part of User
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone=models.IntegerField(default=0)
    male=models.BooleanField(default=False)
    female=models.BooleanField(default=False)
    website=models.URLField(default='')
    image=models.ImageField(upload_to="profile_img",blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance) # create the profile of the User instance

@ receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save() # save the User instance profile
