from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email=models.EmailField(verbose_name='email',max_length=255,unique=True)
    phone=models.IntegerField(null=True)
    profile_photo=models.ImageField(null=True)
    REQUIRED_FIELDS=['username','phone','first_name','last_name','profile_photo']
    USERNAME_FIELD='email'

    def get_username(self):
        return self.email
