from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriesViewSet, ProductViewSet

router = DefaultRouter()
router.register('categories', CategoriesViewSet)
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
