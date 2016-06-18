from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mlearn.models import Mlearn
from mlearn.serializers import MlearnSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
@csrf_exempt
def mlearn_list(request):
    """
    List all mlearn objects, or create a new object.
    """
    if request.method == 'GET':
        mlearns = Mlearn.objects.all()
        serializer = MlearnSerializer(mlearns, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MlearnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT','DELETE'])
@csrf_exempt
def mlearn_detail(request, pk):
    """
    Retrieve, update or delete a mlearn object.
    """
    try:
        mlearn = Mlearn.objects.get(pk=pk)
    except Mlearn.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = MlearnSerializer(mlearn)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MlearnSerializer(mlearn, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mlearn.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)