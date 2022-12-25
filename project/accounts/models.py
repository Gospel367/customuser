from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.utils import timezone
from django.db.models import  UniqueConstraint


class Customuser(AbstractUser):
  customer_id = models.CharField(max_length=10, blank=True)
  address = models.CharField(max_length=255, blank=True)
  phone_number = models.PositiveIntegerField(default = 0000)


  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone_number']

  class Meta:
    #unique_together = ('email',)
    verbose_name ='Custom User'
    verbose_name_plural = 'Custom Users'

  def __str__(self):
    return self.username


UniqueConstraint(
    name='unique_order',
    fields=['email'],
)