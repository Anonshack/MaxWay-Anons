from rest_framework import serializers
from .models import (
    Announcement,
    Product,
    Customer,
    Order,
    Card,
    AboutUs,
    Contact,
)


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'description', 'image']


class ProductSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'cost', 'price', 'image', 'created_at']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'created_at']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'payment_type', 'status', 'address', 'customer', 'created_at']


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'user', 'is_sold', 'added_date']


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['title', 'image', 'info']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['title', 'image', 'url', 'text']
