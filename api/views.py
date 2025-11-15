from django.shortcuts import render
from account.models import ShopUser
from .serializers import *
from rest_framework import generics
from shop.models import Product
from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
# Create your views here.


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShopUserListAPIView(views.APIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [BasicAuthentication]
    def get(self, request, *args, **kwargs):
        users = ShopUser.objects.all()
        serializer = ShopUserSerializer(users, many=True)
        return Response(serializer.data)

class UerRegistrationAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = ShopUser.objects.all()
    serializer_class = UerRegistrationSerializer