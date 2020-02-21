from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

# color status option for public or private 
STATUS = (
    (0,"Private"),
    (1,"Publish")
)

class Palette(models.Model):
    color_name = models.CharField(max_length=25)
    color_domain_one = models.CharField(max_length=25)
    color_domain_two = models.CharField(max_length=25)
    color_accent_one = models.CharField(max_length=25)
    color_accent_two = models.CharField(max_length=25)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['color_name'] #porder by color name

    def __str__(self):
        return self.color_name #return the color name
