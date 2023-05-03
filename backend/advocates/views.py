from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Advocate

@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', '/advocates/:username']
    return Response(data)


def home(request):
    return HttpResponse('<h1>Home</h1>')


def advocates_list(request):
    data = Advocate.objects.all()
    return Response(data, safe=False)

def advocate_detail(request, username):
    data = {"name": username}
    return Response(data)
