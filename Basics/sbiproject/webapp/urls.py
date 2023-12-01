from django.urls import path
from webapp import views

urlpatterns = [
    path('pageone/', views.getpageone),
    path('pagetwo/', views.getpagetwo)
]
