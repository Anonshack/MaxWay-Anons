from django.db import models
from django.contrib.auth import get_user_model


class Announcement(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='announcement/')


class Product(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    cost = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product name: {self.title}"


class Customer(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=100, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Customer name: {self.first_name}"


class Order(models.Model):
    payment_type = models.IntegerField(null=False, blank=False)
    status = models.IntegerField(null=False, blank=False)
    address = models.CharField(max_length=250, null=False, blank=False)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)


class Card(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        related_name="cards",
        on_delete=models.PROTECT,
        default=None
    )
    is_sold = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.added_date}"


class AboutUs(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to='about/', blank=True)
    info = models.TextField(blank=True, null=True)


class Contact(models.Model):
    title = models.CharField(max_length=155, null=False, blank=False)
    image = models.ImageField(upload_to='contact/', blank=True)
    url = models.URLField(verbose_name='Url Link')
    text = models.TextField(blank=True, null=True)
