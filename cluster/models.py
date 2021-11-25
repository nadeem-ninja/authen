from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.user.username
