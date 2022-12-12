from .serializers import *
from .models import Item
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def item_detail_api(request, pk):
    detail_item = Item.objects.get(pk=pk)
    data = ItemSerializers(detail_item).data
    return Response({'data':data})

class ApiItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializers
    queryset = Item.objects.all()