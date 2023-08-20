from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from menu.models import Dish
from menu.forms import DishModelForm


class DishListView(ListView):
    model = Dish
    template_name = 'main_page.html'
    context_object_name = 'dishes'


class DetailDishView(DetailView):
    model = Dish
    template_name = 'info_dish.html'
    context_object_name = 'dish'


class AddDishView(CreateView):
    model = Dish
    template_name = 'add_dish.html'
    form_class = DishModelForm

    def get_success_url(self, **kwargs):
        return reverse('main_page')


class DishUpdateView(UpdateView):
    model = Dish
    template_name = 'update_dish.html'
    form_class = DishModelForm

    def get_success_url(self, **kwargs):
        return reverse('main_page')


class DishDeleteView(DeleteView):
    model = Dish
    template_name = 'delete_dish.html'
    context_object_name = 'dish'

    def get_success_url(self, **kwargs):
        return reverse('main_page')
