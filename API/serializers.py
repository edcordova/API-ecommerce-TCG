from rest_framework import serializers
from .models import Cards, ShoppingCar, User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']


class ReadCardsSerializer(serializers.ModelSerializer):

    owner = UserSerializer(read_only=True)

    class Meta:
        model = Cards
        fields = '__all__'

class WriteCardsSerializer(serializers.ModelSerializer):

    owner = UserSerializer(read_only=True)       

    class Meta:
        model = Cards
        fields = ['owner','name','description','maze','sealed']

class ReadShoppingCarSerializer(serializers.ModelSerializer):

    cardlist = ReadCardsSerializer(many=True)

    class Meta:
        model = ShoppingCar
        fields = ['cardlist']

