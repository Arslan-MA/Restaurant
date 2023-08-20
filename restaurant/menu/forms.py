from django import forms
from menu.models import Dish


class DishModelForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'n_s'}),
            'category': forms.Select(attrs={'class': 'c_s'}),
            'description': forms.Textarea(attrs={'class': 'd_s'}),
            'price': forms.NumberInput(attrs={'class': 'p_s'})
        }
        labels = {
            'name': 'Название блюда',
            'category': 'Категория блюда',
            'description': 'Описание блюда',
            'price': 'Цена блюда'
        }
