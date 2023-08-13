from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class User(AbstractUser):
    USER_TYPE=(
        ('visitor','visitor'),
        ('developer','developer')
        )
    Username=None
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=14)
    is_verified=models.BooleanField(default=False)
    email_token=models.CharField(max_length=100,null=True,blank=True)
    forget_password=models.CharField(max_length=100,null=True,blank=True)
    last_login=models.DateTimeField(null=True,blank=True)
    last_logout_time=models.DateTimeField(null=True,blank=True)
    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','user_type']
    user_type=models.CharField(max_length=100,choices=USER_TYPE,default=USER_TYPE[0])