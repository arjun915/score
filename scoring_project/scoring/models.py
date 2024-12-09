from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='teams',null=True, default=None)

    def __str__(self):
        return f"{self.name} ({self.event.name})"
