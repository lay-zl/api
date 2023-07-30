from django import forms
from .models import Categories,Product


class CategorForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
