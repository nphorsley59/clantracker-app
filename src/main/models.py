from django.db import models


class Player(models.Model):
    tag = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.tag


class PlayerStatusLog(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    exp_level = models.IntegerField()
    town_hall_level = models.IntegerField()

    def __str__(self):
        return self.exp_level
