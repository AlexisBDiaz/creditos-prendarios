
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from django.utils import timezone
import time 
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.usuario.models import User
from apps.usuario.serializers import UserSerializers

# Create your views here.
class UserList(APIView):
    def get(self, request, format=None):
        queryset = User.objects.all()
        serializer = UserSerializers(queryset, many=True)        
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get_object(self, id):
        try:            
            return User.objects.get(id=id) 
        except User.DoesNotExist: 
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = UserSerializers(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request , id, format=None):
        Id = self.get_object(id)
        serializer = UserSerializers(Id, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)