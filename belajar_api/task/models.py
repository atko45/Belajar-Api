from django.db import models

# Create your models here.
class BelajarAPI(models.Model):
	name = models.TextField(default='odading')
	motto = models.TextField(default='pending')
