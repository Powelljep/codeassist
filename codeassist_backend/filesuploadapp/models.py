from django.db import models
from oderapp.models import Order
from programmerapp import Programmer

class FileUpload(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    file = models.FileField(upload_to="/")
    description = models.CharField(max_length=100)


