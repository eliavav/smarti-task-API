from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=100)
    UserAddress = models.CharField(max_length=100)
    UserPhone = models.CharField(max_length=50)

