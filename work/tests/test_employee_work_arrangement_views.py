import json
from decimal import Decimal

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employee.models import Employee
from work.models import WorkArrangement, EmployeeWorkArrangement


class WorkArrangementViewTests(APITestCase):
    def setUp(self):
        """Setting initial data for comparison and duplicate constraint testing"""
        self.list_create_url = reverse('employee-work-arrangement-list-create')
        self.employee = Employee.objects.create(employee_name="Milton", hourly_rate=Decimal(200))
        self.work_arrangement = WorkArrangement.objects.create(work='Data Entry', work_type='FT')
        self.employee_work_arrangement = EmployeeWorkArrangement.objects.create(employee=self.employee,
                                                                                work_arrangement=self.work_arrangement,
                                                                                percentage=50)

    def test_emp_work_arrangement_isinstance(self):
        self.assertTrue(isinstance(self.employee_work_arrangement, EmployeeWorkArrangement))

    def test_emp_work_arrangement_creation(self):
        data = {
            'employee': self.employee.id,
            'work_arrangement': self.work_arrangement.id,
            'percentage': 40
        }
        data = json.dumps(data)
        response = self.client.post(self.list_create_url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_emp_work_arrangement_list(self):
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_emp_work_arrangement_with_invalid_percentage(self):
        employee = Employee.objects.create(employee_name="Haley", hourly_rate=Decimal(200))
        work_arrangement = WorkArrangement.objects.create(work='Data Cleaning', work_type='FT')

        data = {
            'employee': employee.id,
            'work_arrangement': work_arrangement.id,
            'percentage': 110
        }
        data = json.dumps(data)
        response = self.client.post(self.list_create_url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_emp_work_arrangement_with_invalid_total_percentage(self):
        employee = Employee.objects.create(employee_name="Jennifer", hourly_rate=Decimal(300))
        work_arrangement = WorkArrangement.objects.create(work='Employee Management', work_type='FT')
        self.employee_work_arrangement = EmployeeWorkArrangement.objects.create(employee=employee,
                                                                                work_arrangement=work_arrangement,
                                                                                percentage=70)
        data = {
            'employee': employee.id,
            'work_arrangement': work_arrangement.id,
            'percentage': 40
        }
        data = json.dumps(data)
        response = self.client.post(self.list_create_url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_emp_work_arrangement_creation_invalid_employee_id(self):
        data = {
            'employee': 4,
            'work_arrangement': self.work_arrangement.id,
            'percentage': 40
        }
        data = json.dumps(data)
        response = self.client.post(self.list_create_url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_emp_work_arrangement_details(self):
        url = reverse('employee-work-arrangement-retrieve-update-delete',
                      kwargs={'pk': self.employee_work_arrangement.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_emp_work_arrangement_details_invalid_id(self):
        url = reverse('employee-work-arrangement-retrieve-update-delete', kwargs={'pk': 100})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_emp_work_arrangement_update(self):
        data = {
            'percentage': 30
        }
        data = json.dumps(data)
        url = reverse('employee-work-arrangement-retrieve-update-delete',
                      kwargs={'pk': self.employee_work_arrangement.id})
        response = self.client.patch(url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('percentage'), '30.00')

    def test_emp_work_arrangement_update_invalid_percentage(self):
        # percentage = 60 because employee already has 50% work, total_work_percentage > 100 is invalid
        data = {
            'percentage': 60
        }
        data = json.dumps(data)
        url = reverse('employee-work-arrangement-retrieve-update-delete',
                      kwargs={'pk': self.employee_work_arrangement.id})
        response = self.client.patch(url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_emp_work_arrangement_update_invalid_employee(self):
        # percentage = 60 because employee already has 50% work, total_work_percentage > 100 is invalid

        data = {
            'employee': 1000
        }
        data = json.dumps(data)
        url = reverse('employee-work-arrangement-retrieve-update-delete',
                      kwargs={'pk': self.employee_work_arrangement.id})
        response = self.client.patch(url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_emp_work_arrangement(self):
        """Testing employee work arrangement successful delete view"""
        employee = Employee.objects.create(employee_name="Hamilton", hourly_rate=Decimal(200))
        work_arrangement = WorkArrangement.objects.create(work='Office Boy', work_type='FT')
        employee_work_arrangement = EmployeeWorkArrangement.objects.create(employee=employee,
                                                                           work_arrangement=work_arrangement,
                                                                           percentage=50)
        url = reverse('employee-work-arrangement-retrieve-update-delete', kwargs={'pk': employee_work_arrangement.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(EmployeeWorkArrangement.objects.filter(id=employee_work_arrangement.id).exists())

    def test_delete_emp_work_arrangement_invalid(self):
        """Testing employee work arrangement invalid delete view"""
        url = reverse('employee-work-arrangement-retrieve-update-delete', kwargs={'pk': 300})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
