from django.contrib import admin
from django.urls import path
from empapp import views
urlpatterns = [
    path('create', views.createemp),
    path('update/<int:id>', views.updateemp),
    path('', views.getemployees),
    path('delete/<int:id>', views.deleteemp),
    path('display', views.dispalyEmployee)
]
