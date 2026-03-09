from rest_framework import viewsets
from .models import ClothingItem
from .serializers import ClothingItemSerializer

class ClothingItemViewSet(viewsets.ModelViewSet):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer


# Additional API view for outfit recommendation

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def recommend_outfit(request):
    
    top = ClothingItem.objects.filter(category="top").first()
    bottom = ClothingItem.objects.filter(category="bottom").first()
    shoes = ClothingItem.objects.filter(category="shoes").first()

    outfit = {
        "top": top.name if top else "No top available",
        "bottom": bottom.name if bottom else "No bottom available",
        "shoes": shoes.name if shoes else "No shoes available"
    }

    return Response(outfit)