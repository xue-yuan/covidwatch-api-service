from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(blank=False, max_length=50)
    phone = models.CharField(blank=False, null=True, max_length=50)
    school = models.CharField(blank=False, null=True, max_length=50)

    class Meta(AbstractUser.Meta):
        pass

class UploadData(models.Model):
    strength = models.FloatField()
    fk_exp_id = models.IntegerField()
    battery_level = models.IntegerField()