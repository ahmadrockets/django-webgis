from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
  def create_user(self,email,username,nama,password,**other_fields):
    if not email:
      raise ValueError(_("User must have an email address"))
    if not username:
      raise ValueError(_("User must have an unique username"))
    if not password:
      raise ValueError(_("User must have a password"))
    email=self.normalize_email(email)
    user=self.model(email=email,username=username,nama=nama,**other_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_superuser(self,email,username,nama,password,**other_fields):
    other_fields.setdefault('role_id',1)
    if not email:
      raise ValueError(_("User must have an email address"))
    if not username:
      raise ValueError(_("User must have an unique username"))
    if not password:
      raise ValueError(_("User must have a password"))
    email=self.normalize_email(email)
    user=self.model(email=email,username=username,nama=nama,**other_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

class User(AbstractBaseUser):
  user_id = models.AutoField(primary_key=True)
  role_id = models.IntegerField(default=2)
  nama = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  username = models.CharField(max_length=50, unique=True)
  password = models.CharField(max_length=128)
  email = models.CharField(max_length=50, null=True)
  notelp = models.CharField(max_length=50, null=True)
  last_login = models.DateTimeField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  objects = UserManager()
  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['email','nama']

  def __str__(self):
    return self.username 

  class Meta:
        db_table = "users"


class Roles(models.Model):
  nama = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
        db_table = "roles"
