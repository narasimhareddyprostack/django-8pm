from django.urls import path
from userapp import views

urlpatterns = [
    path('index/', views.indexpage),
    path('service/', views.servicepage),
    path('product/', views.productpage),
    path('contact/', views.contactpage),
]
