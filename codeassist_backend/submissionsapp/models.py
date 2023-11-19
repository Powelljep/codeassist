from django.db import models
from filesuploadapp.models import FileUpload

class Submission(models.Model):
    files = models.ManyToManyField(FileUpload, related_name='submissions')
    submitted_at = models.DateTimeField(auto_now_add=True)
