from django.urls import path
from . import views


urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('add-event/', views.add_event, name='add_event'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/add-team/', views.add_team, name='add_team'),
    path('increment-score/<int:team_id>/', views.increment_score, name='increment_score'),
    path('decrement-score/<int:team_id>/', views.decrement_score, name='decrement_score'),
    path('team/<int:team_id>/reset/', views.reset_score, name='reset_score'),

]
