from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:        
        model = User
        fields = ['id', 'fname', 'lname', 'email', 'password', 'phone', 'country_code']
        
# class BookPartialUpdateView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     partial = True