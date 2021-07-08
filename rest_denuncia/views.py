from django.http import request
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.models import Denuncia
from .serializers import DenunciaSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))

def lista_denuncia(request):
    """
    Lista todas las denuncias
    """

    if request.method == 'GET':
        denuncia = Denuncia.objects.all()
        serializer = DenunciaSerializer(denuncia, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        data = JSONParser().parse(request)
        serializer = DenunciaSerializer (data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_denuncia(request, id):
    """
    Get, update, o delete de una denuncia en particular
    """
    try:
        denuncia = Denuncia.objects.get(idDenuncia=id)
    except Denuncia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DenunciaSerializer(denuncia)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DenunciaSerializer(denuncia, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        denuncia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
# Create your views here.
