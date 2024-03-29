from django.db import models
from django.contrib.auth.base_user import BaseUserManager,AbstractBaseUser, make_password
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,username,email,password,**kwargs):
        hashed_password = make_password(password)
        user = self.model(username=username,email=email,password=hashed_password,**kwargs)
        user.save()
        return user


    def create_super_user(self,username,email,password,**kwargs):
        user = self.model(username=username,email=email,**kwargs)
        user.set_password(password)
        user.is_admin = True
        user.save()
        return user



class User(AbstractBaseUser):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    objects = UserManager()
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'





class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bio = models.TextField()
    profession = models.CharField(max_length=30)
    profile_picture = models.ImageField(default="default.jpg")


@receiver(post_save,sender=User)
def user_created(sender,instance,created,**kwargs):
    if created:
        print("profile created")
        Profile.objects.create(user=instance)
    
