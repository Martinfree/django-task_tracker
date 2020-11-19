import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView,
                                     DestroyAPIView,
                                     CreateAPIView)

from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from board.serializers import BoardSerializer,TaskSerializer

from board.models import Board,Task

class BoardsAPIView(APIView):
    permission_classes = [AllowAny]
    queryset = Board.objects.none()
    serializer_class = BoardSerializer

    def get(self,request,*args,**kwargs):
        self.queryset = Board.objects.all()
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardAPIView(APIView):
    lookup_field = 'id'
    permission_classes = [AllowAny]
    queryset = Board.objects.none()
    serializer_class = BoardSerializer
    serializer = BoardSerializer(queryset)

    def get(self,request,*args,**kwargs):
        try:
            self.queryset = Board.objects.get(id=kwargs.get("id"))
            serializer=self.serializer_class(self.queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except (Board.DoesNotExist, TypeError): 
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        return Response(data="METHOD_NOT_ALLOWED", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def put(self,request,*args,**kwargs):
        try:
            self.queryset = Board.objects.get(id=kwargs.get('id'))
            serializer = self.serializer_class(data=request.data)
        except Board.DoesNotExist: 
            return Response(status=status.HTTP_404_NOT_FOUND)
        if serializer.is_valid():
            serializer.update(instance=self.queryset,validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self,request,*args,**kwargs):
        try:
            obj=Board.objects.filter(id=kwargs.get('id'))
            obj.delete()
            return Response(status=status.HTTP_200_OK)
        except Board.DoesNotExist: 
            return Response(status=status.HTTP_404_NOT_FOUND)

