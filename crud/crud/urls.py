
from django.contrib import admin
from django.urls import path
from empapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create', views.createempview),
    path('read', views.displayempview),
    path('edit/<int:id>', views.editempview),
    path('update/<int:id>', views.updateempview),
    path('delete/<int:id>', views.deleteempview),
]
