from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers.serializer import DataSerializer
from appointments.models import Appointments
from django.db.models import Count
# Create your views here.
@api_view(['GET'])
def getData(request):
    
    data = Appointments.objects.values('status').annotate(total=Count('status'))
    serializer = DataSerializer(data, many=True)
    return Response(serializer.data)

# Create your views here.
