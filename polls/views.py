from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from .models import AuthorModel
from .serializer import AuthorSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permission import OwnerPermission
# Create your views here.

class ListAuthorApiView(generics.ListAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,OwnerPermission)


class DetailUpdateDestroyAuthorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,OwnerPermission)