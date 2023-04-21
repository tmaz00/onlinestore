from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Customer


# Function that will execute everytime the user is created
"""
If User is created the signal 'post_save' is generated and being received by
receiver
"""
@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance, 
                                fullname=f'{instance.first_name} {instance.last_name}',
                                email=instance.email)

# Function which saves created Profile
@receiver(post_save, sender=User)
def save_customer(sender, instance, **kwargs):
    instance.customer.save()