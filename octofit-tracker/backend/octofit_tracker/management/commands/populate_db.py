from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team=dc)

        # Create Activities, Leaderboard, Workouts (add your fields as needed)
        Activity.objects.create(user=ironman, type='run', duration=30)
        Activity.objects.create(user=batman, type='cycle', duration=45)
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=batman, points=120)
        Workout.objects.create(user=ironman, description='Chest day')
        Workout.objects.create(user=batman, description='Leg day')

        self.stdout.write(self.style.SUCCESS('Test data created!'))