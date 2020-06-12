from django.db.models.signals import post_save
from .models import a
from django.dispatch import receiver
from .models import Profile


@receiver(post_save,sender=a)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=a)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()




