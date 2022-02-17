from django.db import models
from django.contrib.auth.models import User


class Bookkeep(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.CharField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to=None, height_field=None,
                                    width_field=None, max_length=None, null=True)
