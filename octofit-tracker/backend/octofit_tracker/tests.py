from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Team, Activity, Workout, LeaderboardEntry

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_user_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TeamTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.team = Team.objects.create(name='Test Team')
        self.team.members.add(self.user)

    def test_team_list(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ActivityTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.activity = Activity.objects.create(user=self.user, activity_type='run', duration=30, calories_burned=200, date='2024-01-01')

    def test_activity_list(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class WorkoutTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.workout = Workout.objects.create(user=self.user, name='Morning Workout', description='Pushups and situps', date='2024-01-01')

    def test_workout_list(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class LeaderboardEntryTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.entry = LeaderboardEntry.objects.create(user=self.user, score=100, rank=1)

    def test_leaderboard_list(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
