from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User


# Create your models here.
class User(User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
