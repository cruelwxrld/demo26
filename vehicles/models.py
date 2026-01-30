from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, unique=True, verbose_name="Имя пользователя")
    email = models.CharField(max_length=255, unique=True, verbose_name="Эл. почта пользователя")

class Basket(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="basket_user")

class Country(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название страны")

class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Именование поставщика")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="supplier_country")

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Именование товара")
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="supplier")

class StatusItem(models.Model):
    type_status_order = models.CharField(max_length=50, unique=True, verbose_name="Статус заказа")

class Order(models.Model):
    order_name = models.CharField(max_length=1000, unique=True)
    status = models.ForeignKey(StatusItem, on_delete=models.CASCADE, related_name="status")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_order")
    basket = models.ForeignKey(Basket, on_delete=models.SET_NULL, null=True, blank=True, related_name="order_basket")

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_items")
    price_at_time = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    quantity = models.IntegerField(default=0)

class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name="basket_item")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="basket_items")
    quantity = models.IntegerField(default=0)