from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Users
        User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Teams
        Team.objects.create(name='Team Alpha', members=['alice@example.com', 'bob@example.com'])
        Team.objects.create(name='Team Beta', members=['carol@example.com'])

        # Activities
        Activity.objects.create(user='alice@example.com', activity_type='run', duration=30, date=timezone.now())
        Activity.objects.create(user='bob@example.com', activity_type='walk', duration=45, date=timezone.now())
        Activity.objects.create(user='carol@example.com', activity_type='strength', duration=20, date=timezone.now())

        # Leaderboard
        Leaderboard.objects.create(team='Team Alpha', points=75)
        Leaderboard.objects.create(team='Team Beta', points=20)

        # Workouts
        Workout.objects.create(name='Push Ups', description='Do 20 push ups')
        Workout.objects.create(name='Jogging', description='Jog for 15 minutes')
        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
