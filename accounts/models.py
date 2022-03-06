from django.db import models

# Create your models here
class Contact(models.Model):
    name=models.CharField(max_length=250)
    mobile=models.CharField(max_length=10)
    def __str__(self):
        return self.name