from django.db import models
from users.models import CustomUser
from django.utils.timezone import activate

class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=255, blank=True, null=True)
    complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)
    completed_date = models.DateTimeField(auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.title
