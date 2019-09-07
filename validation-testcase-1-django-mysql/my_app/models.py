from django.db import models


# Create your models here.

class InfoModel(models.Model):
    f_name = models.CharField(max_length=50, unique=True)
    salary = models.IntegerField()

    def __str__(self):
        return self.f_name
