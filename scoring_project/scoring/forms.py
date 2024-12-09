from django import forms
from .models import Event, Team

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']
