# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=20)
    
class Album(models.Model):
    pass

class article(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now)
    publish_date = models.DateTimeField(blank = True,null = True)
    
    def publish(self):
        self.publish_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
    
    def getAllList(self):
        pass


if __name__ == '__main__':
    pass
    
    # FAQ:  Unknown command: 'syncdb'
    
    # Your models have changes that are not yet reflected in a migration, and so won't be applied.
    # Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them    
    