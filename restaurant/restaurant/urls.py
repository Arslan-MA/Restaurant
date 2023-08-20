"""
URL configuration for restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from menu.views import DishListView, DetailDishView, AddDishView, DishUpdateView, DishDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DishListView.as_view(), name='main_page'),
    path('info/dish/<int:pk>', DetailDishView.as_view(), name='info_dish'),
    path('add/', AddDishView.as_view(), name='add_dish'),
    path('update/dish/<int:pk>', DishUpdateView.as_view(), name='update_dish'),
    path('delete/dish/<int:pk>', DishDeleteView.as_view(), name='delete_dish'),
]
