from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField()
    is_email_verified = models.BooleanField(default=False)
