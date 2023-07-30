from rest_framework import serializers
from .models import *


class CategoriesSeralizer(serializers.ModelSerializer):
    #categore = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all())

    class Meta:
        model = Categories
        fields = '__all__'





class ProductSeralizer(serializers.ModelSerializer):
    categories = CategoriesSeralizer(many=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'discription', 'categories')