#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 17:34:51 2018

@author: yanis
"""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from registration.models import Ouruser
from registration.serializers import OuruserSerializer





@api_view(['GET', 'POST'])

def Ouruser_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        ourusers = Ouruser.objects.all()
        serializer = OuruserSerializer(ourusers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OuruserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    

@api_view(['GET', 'PUT', 'DELETE'])
def Ouruser_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        ouruser = Ouruser.objects.get(pk=pk)
    except Ouruser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OuruserSerializer(ouruser)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OuruserSerializer(ouruser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ouruser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
