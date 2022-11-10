import json
from decimal import Decimal

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employee.models import Employee, Team


class EmployeeViewTests(APITestCase):

    def setUp(self):
        self.list_create_url = reverse('employee-list-create')
        self.employee = Employee.objects.create(employee_name="Hugo", hourly_rate=Decimal(200))
        self.team = Team.objects.create(name="ENGINEERING")

    def test_get_employee_list(self):
        """
        Testing employee_list view
        """
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_duplicate_employee_creation(self):
        """
        Testing employee creation with existing name. This will throw a duplicate error
        """
        data = {
            "employee_name": "Hugo",
            "hourly_rate": 250,
        }
        response = self.client.post(self.list_create_url, format='json', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_employee(self):
        """
        Testing employee creation (success - HTTP 201 CREATED)
        """
        data = {
            "employee_name": "John",
            "hourly_rate": 200,
        }
        data = json.dumps(data)
        response = self.client.post(self.list_create_url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['employee_id'], 'EDI-EMP-2')

    def test_invalid_team_id(self):
        """
        Testing employee creation with invalid team id
        """
        data = {
            "employee_name": "John",
            "hourly_rate": 200,
            "team": 2
        }
        data = json.dumps(data)
        response = self.client.post(self.list_create_url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_employee_detail_view(self):
        """
        Testing employee details view
        """
        response = self.client.get(reverse('employee-retrieve-update-delete', kwargs={'pk': self.employee.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['employee_name'], 'Hugo')

    def test_get_invalid_employee_id(self):
        """
        Testing employee detail view with invalid employee id
        """
        response = self.client.get(reverse('employee-retrieve-update-delete', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_employee_team(self):
        """
        Testing update employee team
        """
        team_id = self.team.id
        data = {
            'team': team_id
        }
        data = json.dumps(data)
        url = reverse('employee-retrieve-update-delete', kwargs={'pk': self.employee.id})
        response = self.client.patch(url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.employee.id, team_id)

    def test_update_duplicate_employee_data(self):
        """
        Test updating employee data with already existing details
        """
        new_team = Team.objects.create(name="DATA")
        new_employee = Employee.objects.create(employee_name="Rohit", hourly_rate=Decimal(100))

        data = {
            'employee_name': "Rohit",
            'team': new_team.id
        }
        data = json.dumps(data)
        url = reverse('employee-retrieve-update-delete', kwargs={'pk': self.employee.id})
        response = self.client.patch(url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
