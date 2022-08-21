from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    ph_no = models.IntegerField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    