from .models import Card
from rest_framework import viewsets, permissions
from .serializers import CardSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class CardViewSet(viewsets.ModelViewSet):
    permission_classes = [
		permissions.AllowAny
	]
    queryset = Card.objects.all()
    serializer_class = CardSerializer

@api_view(['GET'])
def health_check(request):
   return Response(
    {"status": "OK", "message": "Backend funcionando correctamente"},
    status=status.HTTP_200_OK
)





