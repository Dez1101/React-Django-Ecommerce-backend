from django.shortcuts import render
from django.http import JsonResponse
from .products import products
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serailizers import ProductSerializer
# Create your views here.

@api_view(['GET'])
def home_view(request):
    routes = [ 
                '/api/productd/',
                '/api/products/create/',

                '/api/products/upload/',
                '/api/<id>/reviews/',

                '/api/products/top/',
                '/api/products/<id>/',

                '/api/products/delete/<id>/',
                '/api/products/<update>/<id>/',
    ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serailizer = ProductSerializer(products, many=True)
    return Response(serailizer.data)



@api_view(['GET'])
def getProduct(request, pk):
   product = Product.objects.get(_id=pk)
   serializer =ProductSerializer(product, many=False)
   return Response(serializer.data)