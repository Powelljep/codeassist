from django.db import models

STACK = (
    ("1", "Front-End Developer"),
    ("2", "Backend-Developer"),
    ("3", "Full Stack Developer")
)
class Programmer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to="images/", default=None)
    email = models.EmailField(max_length=100)
    specialization = models.CharField(max_length=250, choices= STACK, default= '1')
    orders_completed = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
