from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import (
    Announcement,
    Product,
    Customer,
    Order,
    Card,
    AboutUs,
    Contact,
)
from .serializers import (
    AnnouncementSerializer,
    ProductSerializer,
    CustomerSerializer,
    OrderSerializer,
    CardSerializer,
    AboutSerializer,
    ContactSerializer,
)


class AnnouncementListCreateView(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AnnouncementSerializer(queryset, many=True)
        data = {"announcements": serializer.data}
        return Response(data)


class AnnouncementRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AnnouncementSerializer(instance)
        data = {"announcement": serializer.data}
        return Response(data)


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        data = {"products": serializer.data}
        return Response(data)


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductSerializer(instance)
        data = {"product": serializer.data}
        return Response(data)


class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CustomerSerializer(queryset, many=True)
        data = {"customers": serializer.data}
        return Response(data)


class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CustomerSerializer(instance)
        data = {"customer": serializer.data}
        return Response(data)


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = OrderSerializer(queryset, many=True)
        data = {"orders": serializer.data}
        return Response(data)


class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = OrderSerializer(instance)
        data = {"order": serializer.data}
        return Response(data)


class CardListCreateView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CardSerializer(queryset, many=True)
        data = {"cards": serializer.data}
        return Response(data)


class CardRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CardSerializer(instance)
        data = {"card": serializer.data}
        return Response(data)


class AboutListCreateView(generics.ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AboutSerializer(queryset, many=True)
        data = {"abouts": serializer.data}
        return Response(data)


class AboutRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AboutSerializer(instance)
        data = {"about": serializer.data}
        return Response(data)


class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ContactSerializer(queryset, many=True)
        data = {"contacts": serializer.data}
        return Response(data)


class ContactRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ContactSerializer(instance)
        data = {"contact": serializer.data}
        return Response(data)
