from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClothingItemViewSet
from .views import ClothingItemViewSet, recommend_outfit

router = DefaultRouter()
router.register(r'clothes', ClothingItemViewSet)

urlpatterns = [
    path('recommendations/', recommend_outfit),
    path('', include(router.urls)),
]