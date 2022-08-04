from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView, status
from .models import Cards, ShoppingCar,User
from .serializers import ReadCardsSerializer, ReadShoppingCarSerializer, WriteCardsSerializer 
from rest_framework.response import Response

# Create your views here.

class CardsList(APIView):

    def get(self, request):
        cards = Cards.objects.all()
        serializer = ReadCardsSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WriteCardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response (serializer.data)

class CardsDetails(APIView):

    def get(self, request, pk):
        cards = Cards.objects.get(id=pk)
        serializer = ReadCardsSerializer(cards)
        return Response(serializer.data)
    
    def put(self, request, pk):
        cards = Cards.objects.get(id=pk)
        serializer = WriteCardsSerializer(cards, data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data)
    
    def delete(self, request, pk):
        cards = Cards.objects.get(id=pk)
        cards.delete()
        return Response (status=status.HTTP_200_OK)

class ShoppingCar(APIView):
    
    def get(self, request):
        
        car = request.user.shoppingcar
        serializer = ReadShoppingCarSerializer(car)
        return Response (serializer.data)

    def post(self, request):
        pass