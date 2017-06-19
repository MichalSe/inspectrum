from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     team_id = models.TextField(max_length=500, blank=True)
#
#
# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()


# Create your models here.
class States(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # many to one, add func - change user if user deleted
    date_created = models.DateTimeField('date created', auto_now_add=True)
    name = models.CharField(max_length=100)
    css_code = models.TextField(default="")
    url = models.CharField(max_length=500)
    followers = models.ManyToManyField(User, related_name='followers_created')

    class Meta:
        unique_together = ('url', 'owner', 'name')

