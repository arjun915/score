from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Team
from .forms import EventForm, TeamForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'scoring/event_list.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'scoring/add_event.html', {'form': form})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'scoring/event_detail.html', {'event': event})

def add_team(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.event = event
            team.save()
            return redirect('event_detail', pk=event.id)
    else:
        form = TeamForm()
    return render(request, 'scoring/add_team.html', {'form': form, 'event': event})

def increment_score(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    team.score += 1
    team.save()
    return redirect('event_detail', pk=team.event.id)

def decrement_score(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    team.score -= 1
    team.save()
    return redirect('event_detail', pk=team.event.id)

def reset_score(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    team.score = 0
    team.save()
    return redirect('event_detail', pk=team.event.pk)
