from django.db import models
from django.utils import timezone


class Task(models.Model):
    head = models.CharField(max_length=32,blank=False,unique=False)
    description = models.CharField(max_length=256,blank=True)
    release_date = models.DateTimeField(auto_now_add=timezone.now(),editable=False)
    edit_at = models.DateTimeField(auto_now=timezone.now())
    status = models.BooleanField(default=False)
    board = models.ForeignKey("Board",to_field="id",on_delete=models.SET_NULL,null=True,blank=True)

class Board(models.Model):
    name = models.CharField(max_length=32)
    release_date = models.DateTimeField(auto_now_add=timezone.now(),editable=False)
    edit_at = models.DateTimeField(auto_now=timezone.now())

