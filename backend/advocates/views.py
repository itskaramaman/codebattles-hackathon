from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Advocate
from .serializers import AdvocateSerializer

@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', '/advocates/:username']
    return Response(data)


def home(request):
    return HttpResponse('<h1>Home</h1>')


@api_view(['GET'])
def advocates_list(request):
    data = Advocate.objects.all()
    serializer = AdvocateSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def advocate_detail(request, username):
    advocate = Advocate.objects.filter(
                    username=username
                ).first()
    serializer = AdvocateSerializer(advocate)
    return Response(serializer.data)
