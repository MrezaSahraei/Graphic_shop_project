from django.db import models
from shop.models import Product
from account.models import ShopUser
# Create your models here.

class Order(models.Model):
    buyer = models.ForeignKey(ShopUser, on_delete=models.SET_NULL, related_name='orders', null=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=11)
    address = models.TextField()
    postal_code = models.CharField(max_length=15)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']
        indexes = [
            models.Index(fields=['-created_date']),
        ]

    def __str__(self):
        return f'order {self.id}'

    def get_total_cost(self):
        price = 0
        for item in self.items.all():
            price += item.get_total_weight()
        return price

    def get_post_cost(self):
        weight = 0
        for item in self.items.all():
            weight += item.get_total_weight()

        if weight < 1000:
            return 0
        elif 1000 <= weight <= 2000:
            return 0
        else:
            return 0

    def get_final_cost(self):
        price = self.get_post_cost() + self.get_total_cost()
        return price


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=1)
    weight = models.PositiveIntegerField(default=0)


    def __str__(self):
        return str(self.id)

    def get_price(self):
        return self.price * self.quantity

    def get_total_weight(self):
        return self.weight * self.quantity