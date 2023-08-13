# from django.db import models
# from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.hashers import make_password
# User=get_user_model()
# # Create your models here.


# class CustomManager(BaseUserManager):
#     def create_user(self,email,user_name,password,**extra_fields):
#         if not email:
#             raise ValueError('Email adress is required')
#         email=self.normalize_email(email)
#         user=self.model(email=email,user_name=user_name,**extra_fields)
#         user.set_password(make_password(password))
#         user.save(using=self._db)
#         return user
        
#     def Create_superuser(self,email,user_name,password,**extra_fields):
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_superuser',True)
#         extra_fields.setdefault('is_active',True)
#         extra_fields.setdefault('is_verify',True)
#         extra_fields.setdefault('user_type','developer')
        
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('superuser must be is staff=true')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('superuser must be is_superuser=true')
#         if extra_fields.get('is_active') is not True:
#             raise ValueError('superuser must be is_active=true')
#         if extra_fields.get('is_verify') is not True:
#             raise ValueError('superuser must be is_verify=true')
#         if extra_fields.get('user_type') is not True:
#             raise ValueError('superuser must be user_type=true')
        
#         return self.create_user(email,user_name,password,**extra_fields)

# class CustomerUser(AbstractBaseUser,PermissionsMixin):
#     USER_TYPE=(
#         ('visitor','visitor'),
#         ('developer','developer')
#         )
#     email=models.EmailField(unique=True)
#     user_name=models.CharField(max_length=100,unique=True)
#     REQUIRED_FIELDS=['user_name']
#     USERNAME_FIELD='email'
#     user_type=models.CharField(max_length=100,choices=USER_TYPE,default=USER_TYPE[0])
#     is_staff=models.BooleanField(default=False)
#     is_superuser=models.BooleanField(default=False)
#     is_active=models.BooleanField(default=False)
#     is_verify=models.BooleanField(default=False)
    
#     objects=CustomManager()
    
#     def __str__(self):
#         return str(self.email)