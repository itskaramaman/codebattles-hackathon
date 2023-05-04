from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.db.models import Q

from .models import Advocate
from .serializers import AdvocateSerializer

@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', '/advocates/:username']
    return Response(data)


@api_view(['GET', 'POST'])
def advocates_list(request):
    # Handles Get request
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            data = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        else:
            data = Advocate.objects.all()
        serializer = AdvocateSerializer(data, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        advocate = Advocate.objects.create(
                        username = request.data['username'],
                        name = request.data['name'],
                        bio = request.data['bio'],
                        twitter = request.data['twitter'],
                    )
        serializer = AdvocateSerializer(advocate)
        return Response(serializer.data)


class AdvocateDetail(APIView):
    """
    Each Advocate details
    """

    def get_object(self, username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            raise Response('Advocate does not exist')
            

    def get(self, request, username):
        advocate = self.get_object(username)
        
        serializer = AdvocateSerializer(advocate)
        return Response(serializer.data)
    
    def put(self, request, username):
        advocate = self.get_object(username)
        advocate.username = request.data['username']
        advocate.name = request.data['name']
        advocate.bio = request.data['bio']
        advocate.twitter = request.data['twitter']

        serializer = AdvocateSerializer(advocate)
        return Response(serializer.data)
    
    def delete(self, request, username):
        advocate = self.get_object(username)
        advocate.delete()
        return Response('user was deleted')
    
