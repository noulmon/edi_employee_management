import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employee.models import Team


class TeamViewTests(APITestCase):
    def setUp(self):
        """Setting initial data for comparison and duplicate constraint testing"""
        self.list_create_url = reverse('team-list-create')
        self.team = Team.objects.create(name='Engineering')

    def test_get_team_list(self):
        """Testing team list API"""
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_team(self):
        """Testing team successful creation"""
        data = {
            'name': 'Auditing'
        }
        data = json.dumps(data)
        response = self.client.post(self.list_create_url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_duplicate_team(self):
        """Testing invalid team creation with duplicate data"""
        data = {
            'name': 'Engineering'
        }
        data = json.dumps(data)
        response = self.client.post(self.list_create_url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signal_created_team_code(self):
        """Testing if the team code is generated using signal, whenever a team instance is created"""
        data = {
            'name': 'Quality Analysis'
        }
        data = json.dumps(data)
        response = self.client.post(self.list_create_url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['code'], 'EDI-TM-2')

    def test_update_team_name(self):
        """Test update team name"""
        data = {
            'name': 'Data Engineering'
        }
        data = json.dumps(data)
        url = reverse('team-retrieve-update-delete', kwargs={'pk': self.team.id})
        response = self.client.patch(url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_team(self):
        """Test delete team"""
        team = Team.objects.create(name='HR')
        url = reverse('team-retrieve-update-delete', kwargs={'pk': team.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Team.objects.filter(name='HR').exists())
