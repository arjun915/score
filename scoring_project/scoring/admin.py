from django.contrib import admin
from .models import Event, Team

admin.site.register(Event)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'score', 'event')
