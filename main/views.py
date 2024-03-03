from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from main.models import Room

def get_rooms(request):
    try:
        rooms = Room.objects.all().get()
    except ObjectDoesNotExist:
        pass

    return render(request, 'rooms.html', {'rooms': rooms})

#create room then redirect to lobby?? yes
def create_room(request):
    pass#redirect

def get_room(request):
    return render(request, 'room.html', {'room': []})