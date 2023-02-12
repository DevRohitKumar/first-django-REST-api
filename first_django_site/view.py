from django.http import JsonResponse
from .models import User
from .serializer import UserSerializer
from rest_framework.decorators import api_view

@api_view()
def get_all_users(request):
    if request.method == 'GET':
        user = User.objects.all() #get all users
        serializer = UserSerializer(user, many=True) #serialize all the users
        return JsonResponse(serializer.data, safe= False) #return json
    