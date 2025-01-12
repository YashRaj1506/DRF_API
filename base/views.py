from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

from .models import Advocate, Company
from .serializers import AdvocateSerializer,  CompanySerializer


@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)

@api_view(['GET', 'POST'])
def advocate_list(request):

    if request.method == 'GET':
        query = request.GET.get('query')

        if query == None:
            query = ''

        print('Query:', query)
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains = query))
        serializer = AdvocateSerializer(advocates, many= True)
        print(advocates)
        return Response(serializer.data)
    
    if request.method == 'POST':

        advocate = Advocate.objects.create(
            username= request.data['username'],
            bio = request.data['bio']
  
            )
        serializer = AdvocateSerializer(advocate, many = False)

        return Response(serializer.data)
    

    
class AdvocateDetail(APIView):

    def get_object(self, username):
        try:
            return Advocate.objects.get(username = username)
        except Advocate.DoesNotExist:
            raise JsonResponse('Advocate doesnt exists')

    # def get(self, request, username):
    #     advocate = Advocate.objects.get(username= username)
    #     serializer = AdvocateSerializer(advocate, many = False)
    #     return Response(serializer.data)  

    def get(self, request, username):
        advocate = self.get_object(username)
        print(advocate)
        serializer = AdvocateSerializer(advocate, many = False)
        return Response(serializer.data)  
        
    def put(self, request, username):
        advocate = self.get_object(username)

        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        serializer = AdvocateSerializer(advocate, many = False)
        return Response(serializer.data)    
    
    def delete(self, request, username):
        advocate = self.get_object(username)
        advocate.delete()
        return Response('user was deleted')


    

# @api_view(['GET', 'PUT', 'DELETE'])
# def advocate_details(request, username):
#     advocate = Advocate.objects.get(username= username)

#     if request.method == 'GET':    
#         serializer = AdvocateSerializer(advocate, many = False)
#         # data = username
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']

#         advocate.save()

#         serializer = AdvocateSerializer(advocate, many = False)
#         return Response(serializer.data)   

#     if request.method == 'DELETE':
#         advocate.delete()
#         return Response('user was deleted')
    





@api_view(['POST'])
def add_advocate(request):
    Advocate.objects.create(
        username= request.data('username')

    )
    return Response

@api_view(['GET'])
def companies_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many = True)
    return Response(serializer.data)
