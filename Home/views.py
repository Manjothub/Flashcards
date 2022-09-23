from django.shortcuts import render
from .models import *



def INDEX(request):
    cards = Card.objects.all().order_by("box", "-date_created")
    context ={
        'card_list':cards
    }
    return render(request,'main/card_list.html',context)


