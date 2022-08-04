from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class User(AbstractUser):
    pass

    

class Cards(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    name = models.CharField(max_length=200)
    description = models.TextField(null=False, blank=False)
    maze = models.CharField(max_length=200)
    maze_date = models.DateField
    sealed = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class ShoppingCar(models.Model):

    owner = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    cardlist = models.ManyToManyField(Cards, blank=True)

    @receiver(post_save, sender=User)
    def create_user_shoppingcar(sender, instance, created, **kwargs):
        if created:
            ShoppingCar.objects.create(owner=instance)

    def __str__(self):
        return f'ShoppingCar_{self.owner}'

    def addToCar(self, item):
        
        self.cardlist.add(item)