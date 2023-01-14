from django.db import models
from django.template.defaultfilters import slugify

from users.models import User
# Create your models here.
class Task(models.Model):
    task_types = [
        ('edu', 'education'),
        ('job', 'job'),
        ('per', 'personal'),
        ('fam', 'family')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=3, choices=task_types, default='per')
    title = models.CharField(max_length=120, null=True)
    done = models.BooleanField(default=False)
    slug = models.SlugField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.title} : {self.user}'

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = self.slug or slugify(self.title[:11])
        super().save()