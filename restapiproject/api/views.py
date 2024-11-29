from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializers, ItemSerializers_allFields

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    
    ## without serializer
    # items_data = []
    # for item in items:
    #     single_product = {
    #         "id": item.id,
    #         "item_name": item.name,
    #         "price": item.price,
    #         "Created_Date": item.created_at
    #     }

    #     items_data.append(single_product)
    # return Response(items_data)
    
    serializer = ItemSerializers_allFields(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)
