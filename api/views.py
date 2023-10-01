from rest_framework import decorators, response
from base.models import Diaspora
from .serializers import DiasporaSerializer

@decorators.api_view(['GET'])
def DiasporaList(request):
    diaspora = Diaspora.objects.all()
    serializer = DiasporaSerializer(diaspora, many=True)

    return response.Response(serializer.data)


@decorators.api_view(['POST'])
def addDiaspora(request):
    new_diaspora = request.data
    serializer = DiasporaSerializer(data=new_diaspora, many=True)
    if serializer.is_valid():
        serializer.save()
    
    return response.Response(serializer.data)
