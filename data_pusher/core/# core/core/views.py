# core/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Account, Destination
from .serializers import AccountSerializer, DestinationSerializer
import requests

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

@api_view(['POST'])
def data_handler(request):
    secret_token = request.headers.get('CL-X-TOKEN')
    if not secret_token:
        return Response({'error': 'CL-X-TOKEN header is missing'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        account = Account.objects.get(app_secret_token=secret_token)
    except Account.DoesNotExist:
        return Response({'error': 'Invalid secret token'}, status=status.HTTP_404_NOT_FOUND)

    data = request.data

    for destination in account.destinations.all():
        headers = destination.headers
        if destination.http_method == 'GET':
            response = requests.get(destination.url, headers=headers, params=data)
        elif destination.http_method == 'POST':
            response = requests.post(destination.url, headers=headers, json=data)
        elif destination.http_method == 'PUT':
            response = requests.put(destination.url, headers=headers, json=data)

    return Response({'status': 'Data sent to all destinations'}, status=status.HTTP_200_OK)
