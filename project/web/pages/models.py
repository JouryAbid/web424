from django.db import models

# Create your models here.


class product (models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default='null')


    def __str__(self):
        return self.name