from django.db import models

# Create your models here.

class Categories(models.Model):
    new_catagory = models.CharField(max_length=100,null=True,blank=True)
    categore = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='categories')

    def __str__(self):
        return str(self.new_catagory)



class Product(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    discription = models.TextField()
    categories = models.ManyToManyField(Categories,related_name='product')

    def __str__(self):
        return self.name

