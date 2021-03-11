from django.shortcuts import render
from api.serializers import DetailSerializer
from api.models import Details

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


# Create your views here.

class DetailsListApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the details
        '''
        details = Details.objects.all()
        serializer = DetailSerializer(details, many=True)
        return Response(serializer.data)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the details object with given  data
        '''
        data = {
            'fname': request.data.get('fname'),
            'lname': request.data.get('lname'),
        }
        serializer = DetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
