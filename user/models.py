from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_of_person = models.CharField(max_length=255)
    address_details = models.TextField()
    mobile_no = models.CharField(max_length=15)
    address_type = models.CharField(max_length=255, choices=[('Home', 'Home'), ('Work', 'Work')])

    def __str__(self):
        return self.name_of_person


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Added this line


    def __str__(self):
        return self.user.username




