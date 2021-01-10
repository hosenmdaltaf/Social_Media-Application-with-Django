
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




#With the @receiver decorator, we can link a signal with a function.
#  So, every time that a User model instance ends to run its save() method (or when user register ends), the update_profile_signal will start to work right after user saved.

#sender - The model class.
#instance - The actual instance being saved.
#created - A boolean; True if a new record was created.

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):     
    instance.profile.save()