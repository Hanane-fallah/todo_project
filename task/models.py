from django.db import models
from users.models import Users
# Create your models here.
class Task(models.Model):
    task_types = [
        ('edu', 'education'),
        ('job', 'job'),
        ('per', 'personal'),
        ('fam', 'family')
    ]
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=3, choices=task_types, default='per')
    title = models.CharField(max_length=120, null=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} : {self.user}'
