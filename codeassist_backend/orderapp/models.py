from django.db import models
from customerapp.models import Customer
from programmerapp.models import Programmer

ODER_CATEGORY = (
    ("1", "Web Developement"),
    ("2", "Mobile App Developement"),
    ("3", "Algorithms"),
)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    category = models.CharField(max_length=50, choices=ODER_CATEGORY, default="1")
    size = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    time_completed = models.DateTimeField()
    urls = models.URLField(default=None)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    


