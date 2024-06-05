from django.db import models

class Apartment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='apartments/', default='./static/images/home.jpeg') 
    is_for_sale = models.BooleanField(default=False)
    is_for_rent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
