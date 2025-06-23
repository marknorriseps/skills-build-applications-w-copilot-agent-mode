# Views for OctoFit Tracker
from rest_framework import viewsets
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'https://crispy-space-meme-9vp7pwg5qq637gvg-8000.app.github.dev' if 'crispy-space-meme-9vp7pwg5qq637gvg-8000.app.github.dev' in request.get_host() else request.build_absolute_uri('/')[:-1]
    return Response({
        'users': f'{base_url}/api/users/',
        'teams': f'{base_url}/api/teams/',
        'activity': f'{base_url}/api/activity/',
        'leaderboard': f'{base_url}/api/leaderboard/',
        'workouts': f'{base_url}/api/workouts/',
    })
