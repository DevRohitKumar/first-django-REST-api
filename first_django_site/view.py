from django.http import JsonResponse
from .models import User
from .serializer import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view() #by default api_view uses ['GET']
def get_all_users(request):
    if request.method == 'GET':
        user = User.objects.all() #get all users
        serializer = UserSerializer(user, many=True) #serialize all the users
        return JsonResponse(serializer.data, safe= False) #return json
    else: 
        return Response({"message": "Something went wrong 🙁" })
    
@api_view()
def get_single_user(request, id):
    if request.method == 'GET':
        try:
            user = User.objects.get(pk = id)
        except User.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user) #serialize 
        return Response(serializer.data) #return json
    else: 
        return Response({"message": "Something went wrong 🙁" })

@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save() #saving data to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({"message": "Something is wrong ☹️"})
    
@api_view(['PUT'])
def update_user(request, id):
    if request.method == 'PUT':
        try:
            user = User.objects.get(pk = id)
            serializer = UserSerializer(user, data= request.data) #serialize 
        except User.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
                
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) #return json
        else:
            return Response({"message": serializer.errors ,
                             "status": status.HTTP_404_NOT_FOUND })
    else: 
        return Response({"message": "Something went wrong 🙁" })
    
    
@api_view(['DELETE'])
def delete_user(request, id):
    if request.method == 'DELETE':
        try:
            user = User.objects.get(pk = id)
        except User.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
                
        if user:
            user.delete()
            return Response({"message": "User deleted successfully",
                             "status": status.HTTP_204_NO_CONTENT }) 
        else:
            return Response({"message": "No such user exists" ,
                             "status": status.HTTP_404_NOT_FOUND })








    
   
'''
Author 👨‍🔬: Rohit Kumar
Email ✉️: contactdevrk@gmail.com
Created 📆: 12-02-2023
'''