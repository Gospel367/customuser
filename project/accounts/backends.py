from django.contrib.auth.backends import ModelBackend
#from django.contrib.auth.models import User as Customuser
from .models import *


class CustomerBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['username']
        password = kwargs['password']
        try:
            customer = Customuser.objects.get(email=email)
            if customer.check_password(password) is True:
                return customer
        except User.DoesNotExist:
            pass

class IdBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        customer_id = kwargs['username']
        password = kwargs['password']
        try:
            customer = Customuser.objects.get(customer_id=customer_id)
            if customer.check_password(password) is True:
                return customer
        except User.DoesNotExist:
            pass