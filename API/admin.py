from django.contrib import admin
from .models import User,Cards,ShoppingCar
# Register your models here.

admin.site.register(User)
admin.site.register(Cards)
admin.site.register(ShoppingCar)