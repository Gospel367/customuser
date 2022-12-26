''''from django.db.models import signals
from django.dispatch import receiver
from .models import Customuser, Profile
from django.db.models.signals import pre_save, post_save


# pre_save method signal
@receiver(pre_save, sender=Customuser)
def user_address(sender, instance, **kwargs):
    if not instance.address:
        instance.description = 'Update your residential address'
        

# post_save method
@receiver(post_save, sender=Customuser) 
def create_profile(sender, instance, created, updated, **kwargs):
    if not updated and created and instance.is_active ==True:
        Profile.objects.create(user_email = instance.email, full_name = f"{instance.first_name} {instance.last_name}", address = instance.address,
        hobby = 'No hobby yet', phone_number = instance.phone_number, marital_status ='single or married?' ) 

    elif updated and instance.is_active ==True:
        Profile.objects.update()

'''