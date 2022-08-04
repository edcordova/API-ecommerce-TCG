from django.urls import path, include
from .views import CardsList, CardsDetails, ShoppingCar

urlpatterns = [
    path('cards/', CardsList.as_view(), name = 'cards' ),
    path('cards/<str:pk>', CardsDetails.as_view(), name = 'cards-detail' ),
    path('shoppingcar/', ShoppingCar.as_view(), name = 'shoppingcar' ),
    
]