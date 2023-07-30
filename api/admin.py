from django.contrib import admin
from .models import Categories, Product


# Register your models here.
@admin.register(Categories)
class CatagrModel(admin.ModelAdmin):
    list_display = ['id', 'new_catagory', 'categore','categore_id']


@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'discription']
