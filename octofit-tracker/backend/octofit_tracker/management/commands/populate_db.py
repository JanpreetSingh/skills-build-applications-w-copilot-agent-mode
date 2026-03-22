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

        # Teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User.objects.create(email='captain@marvel.com', name='Captain America', team='marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='dc'),
            User.objects.create(email='superman@dc.com', name='Superman', team='dc'),
        ]

        # Activities
        Activity.objects.create(user='Iron Man', type='run', duration=30)
        Activity.objects.create(user='Captain America', type='cycle', duration=45)
        Activity.objects.create(user='Batman', type='swim', duration=25)
        Activity.objects.create(user='Superman', type='fly', duration=60)

        # Leaderboard
        Leaderboard.objects.create(user='Iron Man', score=100)
        Leaderboard.objects.create(user='Captain America', score=90)
        Leaderboard.objects.create(user='Batman', score=95)
        Leaderboard.objects.create(user='Superman', score=110)

        # Workouts
        Workout.objects.create(name='Super Strength', description='Strength workout for heroes')
        Workout.objects.create(name='Flight Training', description='Flight skills for Superman')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
