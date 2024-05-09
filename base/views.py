from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

from .models import Advocate
from .serializers import AdvocateSerializer



@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)

@api_view(['GET'])
def advocate_list(request):
    # data = ['Dennis', 'Tadas', 'Max']
    query = request.GET.get('query')

    if query == None:
        query = ''

 
    

    print('Query:', query)
    advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains = query))
    serializer = AdvocateSerializer(advocates, many= True)
    print(advocates)
    return Response(serializer.data)

@api_view(['GET'])
def advocate_details(request, username):
    advocate = Advocate.objects.get(username= username)
    serializer = AdvocateSerializer(advocate, many = False)
    data = username
    return Response(serializer.data)