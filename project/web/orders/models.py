from django.db import models
from django.contrib.auth.models import User
from pages.models import product


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    details = models.ManyToManyField(product,through= 'OrderDetailes') 
    is_finished = models.BooleanField()

    def __str__(self):
        return 'User: '+ self.user.username + ', Order ID: '+ str(self.id)
    

class OrderDetailes(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete= models.CASCADE)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    qty = models.IntegerField()


    def __str__ (self):
        return 'User: '+ self.order.user.username + ', Product: '+ self.product.name +', Order ID: '+ str(self.order.id)
     

