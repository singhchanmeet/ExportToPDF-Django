from django.db import models
import os
from django.utils.html import mark_safe

# Create your models here.
class MyForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=10)
    photograph = models.ImageField(upload_to='photographs')

    def __str__(self):         # for showing record by name in admin panel
        return (self.name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.photograph.url}" width = "100"/>')