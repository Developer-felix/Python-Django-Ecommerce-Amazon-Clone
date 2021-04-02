from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    user_type_choices = ((1, "Admin"), (2, "Staff"), (3, "Merchant"), (4, "Customer"),)
    user_type = models.CharField(max_length=255, choices=user_type_choices, default=1)

class AdminUser(models.Model):
    profile_pic = models.FileField(default="")
    created_at = models.DateTimeField(auto_now_add = True)

class Staff(models.Model):
    profile_pic = models.FileField(default="")
    created_at = models.DateTimeField(auto_now_add=True)

class Merchant(models.Model):
    profile_pic = models.FileField(default="")
    company_name = models.CharField(max_length=255)
    gst_details = models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class CustomerUser(models.Model):
    profile_pic = models.FileField(default="")
    created_at = models.DateTimeField(auto_now_add = True)  