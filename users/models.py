from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(blank=False, null=True, max_length=20)
    phone = models.CharField(blank=False, null=True, max_length=10)
    school = models.CharField(blank=False, null=True, max_length=30)
    token = models.CharField(null=True, max_length=44)
    expire_time = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
    uuid = models.CharField(null=True, max_length=100)
    last_api_calling = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    class Meta(AbstractUser.Meta):
        pass

class TCN_RX(models.Model):
    tx_muuid = models.CharField(max_length=100)
    rx_muuid_short = models.CharField(null=True, max_length=100)
    tx_muuid_short = models.CharField(null=True, max_length=100)
    rx_tcn = models.CharField(max_length=100)
    tcn = models.CharField(max_length=100)
    rssi = models.FloatField()
    distance = models.FloatField()
    unix_timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    upload_timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    exp_id = models.CharField(null=True, max_length=2)
    latitude = models.FloatField()
    longitude = models.FloatField()
    power = models.FloatField()

class TCN_TX(models.Model):
    tx_muuid_short = models.CharField(null=True, max_length=100)
    tx_muuid = models.CharField(max_length=100)
    tx_tcn = models.CharField(max_length=100)
    own_tcn = models.CharField(max_length=100)
    battery_level = models.IntegerField()
    motion_status = models.BooleanField()
    gps_status = models.BooleanField()
    unix_timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    upload_timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    exp_id = models.CharField(null=True, max_length=2)

class AttackLog(models.Model):
    blind_log = models.TextField(null=True)
    unix_timestamp = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

class GlobalSetting(models.Model):
    exp_id = models.CharField(null=True, max_length=2)
