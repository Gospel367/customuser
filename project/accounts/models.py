from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.utils import timezone
from django.db.models import  UniqueConstraint
from django.conf import settings


class Customuser(AbstractUser):
  customer_id = models.CharField(max_length=10, blank=True)
  address = models.CharField(max_length=255, blank=True)
  phone_number = models.PositiveIntegerField(default = 0000)


  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone_number']

  class Meta:
    unique_together = ('email',)
    verbose_name ='Custom User'
    verbose_name_plural = 'Custom Users'


  def __str__(self):
    return self.username


  '''UniqueConstraint(
    name='unique_order',
    fields=['email'],
)'''


  def save(self, *args, **kwargs):
    if self._state.adding:
      Profile.objects.create(user_email = self.email, full_name = f"{self.first_name} {self.last_name}", address = self.address,
        hobby = 'No hobby yet', phone_number = self.phone_number, marital_status ='single or married?' ) 
    return super(Customuser, self).save(*args, **kwargs)



class Profile(models.Model):
  user_email = models.EmailField(max_length=255, blank=True)
  full_name = models.CharField(max_length=255, blank=True)
  address = models.CharField(max_length=255, blank=True)
  phone_number = models.PositiveIntegerField()
  hobby = models.CharField(max_length=255, blank=True)
  marital_status = models.CharField(max_length=255, blank=True)


  def __str__(self):
    return self.full_name

