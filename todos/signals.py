from django.db.models.signals import pre_save, post_save
from .views import Task
from django.dispatch import receiver
from datetime import datetime

@receiver(post_save, sender=Task)
def completed_date(sender, update_fields, instance, **kwargs):
    taskid = instance.id
    if instance.complete == True:
        Task.objects.filter(pk=taskid).update(completed_date=datetime.now())
    elif instance.complete == False:
        Task.objects.filter(pk=taskid).update(completed_date=None)


