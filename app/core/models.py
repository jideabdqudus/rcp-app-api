"""
Database models
"""

from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
  AbstractBaseUser,
  BaseUserManager,
  PermissionsMixin
)


class UserManager(BaseUserManager):
  """Manage for users user"""
  def create_user(self, email, password=None, **extra_field):
    """Create, save and return a new user"""
    if not email:
      raise ValueError('User must have an email address.')
    user = self.model(email=self.normalize_email(email), **extra_field)
    user.set_password(password)
    user.save(using=self._db)

    return user

  def create_superuser(self, email, password):
    """Create and return a new super user"""
    user=self.create_user(email, password)
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)

    return user




class User(AbstractBaseUser, PermissionsMixin):
  """User in the system"""
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255) # Provides a character field, with max length of 255
  is_active = models.BooleanField(default=True) # Boolean field that defaults to true when the user registers
  is_staff = models.BooleanField(default=False) # isStaff is used to determine if the user can login into the admin

  objects = UserManager()

  USERNAME_FIELD = 'email' # Sets the default field to email, and not username


class Recipe(models.Model):
  """Recipe object"""

  # Belongs to this particular user, basically the model is attached to this user
  user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete= models.CASCADE, #If the related object gets deleted, it should also delete everything attached to their user = (models.CASCADE)
  )
  title = models.CharField(max_length=255)
  description = models.TextField(blank=True) #TextField can hold more content with multiple lines
  time_minutes = models.IntegerField()
  price = models.DecimalField(max_digits=5, decimal_places=2)
  link = models.CharField(max_length=255, blank=True)
  tags = models.ManyToManyField("Tag")


  def __str__(self):
    return self.title



class Tag(models.Model):
  """Tag for filtering recipes"""
  name = models.CharField(max_length=250)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  def __str__(self):
      return self.name
