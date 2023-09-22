from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.



class AuthorModel(models.Model):
    name = models.CharField(max_length=100,default='')
    birthday = models.DateTimeField(default=datetime.now)
    career = models.CharField(max_length=200,default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    class Meta:
        db_table = "AuthorModel"
    def __str__(self) -> str:
        return self.name