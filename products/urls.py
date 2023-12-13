from django.urls import path
from .views import (
    AnnouncementListCreateView,
    AnnouncementRetrieveUpdateDestroyView,
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
    CustomerListCreateView,
    CustomerRetrieveUpdateDestroyView,
    OrderListCreateView,
    OrderRetrieveUpdateDestroyView,
    CardListCreateView,
    CardRetrieveUpdateDestroyView,
    AboutListCreateView,
    AboutRetrieveUpdateDestroyView,
    ContactListCreateView,
    ContactRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('announcements/', AnnouncementListCreateView.as_view(), name='announcement-list-create'),
    path('announcements/<int:pk>/', AnnouncementRetrieveUpdateDestroyView.as_view(),
         name='announcement-retrieve-update-destroy'),

    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),

    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-retrieve-update-destroy'),

    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-retrieve-update-destroy'),

    path('cards/', CardListCreateView.as_view(), name='card-list-create'),
    path('cards/<int:pk>/', CardRetrieveUpdateDestroyView.as_view(), name='card-retrieve-update-destroy'),

    path('abouts/', AboutListCreateView.as_view(), name='about-list-create'),
    path('abouts/<int:pk>/', AboutRetrieveUpdateDestroyView.as_view(), name='about-retrieve-update-destroy'),

    path('contacts/', ContactListCreateView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', ContactRetrieveUpdateDestroyView.as_view(), name='contact-retrieve-update-destroy'),
]
