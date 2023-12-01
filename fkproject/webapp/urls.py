from django.urls import path
from webapp import views

urlpatterns = [
    path('index/', views.getindexpage),
    path('contact/', views.getcontactpage)
]
