from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=255)

class Room(models.Model):
    #maybe room settings??
    current_round = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RoomPlayer(models.Model):
    order = models.IntegerField()
    gold = models.IntegerField()
    win_points = models.IntegerField()
    rubies = models.IntegerField()

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

class Ingridient(models.Model):
    name = models.CharField(max_length=255)
    cost = models.IntegerField()
    steps = models.IntegerField()

# current player bought items
class Inventory(models.Model):
    room_player = models.ForeignKey(RoomPlayer, on_delete=models.CASCADE)
    ingridient = models.ForeignKey(Ingridient, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Boiler(models.Model):
    start_position = models.IntegerField()
    drop = models.IntegerField()
    rat_tail = models.IntegerField()
    matrix = models.TextField() #json
    room_player = models.ForeignKey(RoomPlayer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
