from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Mlearn(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    experiment_text = models.TextField()

    class Meta:
    	ordering = ('created',)


