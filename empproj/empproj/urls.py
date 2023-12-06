
from django.contrib import admin
from django.urls import path
from empapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.gethomepage),
    path('newemp/', views.getempregpage),
    path('newuser/', views.getuserregpage),
]
