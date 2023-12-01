from django.urls import path
from webapp import views

urlpatterns = [
    path('index/', views.getindexpage),
    path('service/', views.getservicepage),
    path('about/', views.getaboutpage),
    path('contact/', views.getcontactpage),
]
