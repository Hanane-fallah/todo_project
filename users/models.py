from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True, primary_key=True)
    email = models.EmailField()
    profile_image = models.ImageField(upload_to='images', default='Screenshot_from_2023-01-07_20-45-18.png')

    def __str__(self):
        return self.username

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if '.ac.ir' not in self.email:
            return 
        else:
            self.username = self.username.lower()
            super().save()
