from django.contrib import admin
from .models import (
    Announcement,
    Product,
    Customer,
    Order,
    Card,
    AboutUs,
    Contact,
)
# Register your models here.
models = [Announcement, Product, Customer, Order, Card, AboutUs, Contact]
for clay in models:
    admin.site.register(clay)
