import json
from decimal import Decimal

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employee.models import Team, Employee, TeamLeader


class TeamLeaderViewTests(APITestCase):
    def setUp(self):
        """Setting initial instances for comparison and duplicate constraint test"""
        self.list_create_url = reverse('teamleader-list-create')
        self.employee = Employee.objects.create(employee_name="Hugo", hourly_rate=Decimal(200))
        self.team = Team.objects.create(name="Engineering")
        self.team = TeamLeader.objects.create(employee=self.employee, team=self.team)

    def test_get_team_leader_list(self):
        """Testing team leader list API"""
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_team_leader(self):
        """Testing successful team leader create API"""
        employee = Employee.objects.create(employee_name="John", hourly_rate=Decimal(200))
        team = Team.objects.create(name="Data")

        data = {
            "employee": employee.id,
            "team": team.id
        }
        data = json.dumps(data)
        response = self.client.post(self.list_create_url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_duplicate_team_leader(self):
        """Testing if duplicate data can be created"""
        data = {
            "employee": self.employee.id,
            "team": self.team.id
        }
        data = json.dumps(data)
        response = self.client.post(self.list_create_url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_team_leader_with_invalid_employee(self):
        """Testing if invalid employee id can be used for creating"""
        team = Team.objects.create(name="Data")

        data = {
            "employee": 100,
            "team": team.id
        }
        data = json.dumps(data)
        response = self.client.post(self.list_create_url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_team_leader_with_invalid_data(self):
        """Testing if invalid employee id and team id can be used"""
        data = {
            "employee": 100,
            "team": 200
        }
        data = json.dumps(data)
        response = self.client.post(self.list_create_url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
