# import json
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from work.models import WorkArrangement


class WorkArrangementViewTests(APITestCase):
    def setUp(self):
        """Setting initial data for comparison and duplicate constraint testing"""
        self.list_create_url = reverse('work-arrangement-list-create')
        self.work_arrangement = WorkArrangement.objects.create(work='Data Entry', work_type='FT')

    def test_get_work_arrangement_list(self):
        """Testing team leader list API"""
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_work_arrangement(self):
        """Testing create work arrangement API"""
        data = {
            "work": 'Project Management',
            "work_type": 'FT'
        }
        data = json.dumps(data)
        response = self.client.post(self.list_create_url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_duplicate_work_arrangement(self):
        """Test creating duplicate work arrangement API"""
        data = {
            "work": self.work_arrangement.work,
            "work_type": self.work_arrangement.work_type
        }
        data = json.dumps(data)
        response = self.client.post(self.list_create_url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_work_arrangement_with_invalid_work_type(self):
        """Testing create work arrangement with an invalid work type option"""
        data = {
            "work": 'Taxing',
            "work_type": 'OT'
        }
        data = json.dumps(data)
        response = self.client.post(self.list_create_url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_work_arrangement_detail_view(self):
        """Testing work arrangement detail view"""
        work_arrangement = WorkArrangement.objects.create(work='Auditing', work_type='FT')
        url = reverse('work-arrangement-retrieve-update-delete', kwargs={'pk': self.work_arrangement.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_work_arrangement_detail_view_invalid_id(self):
        """Testing work arrangement detail view with an invalid key"""
        url = reverse('work-arrangement-retrieve-update-delete', kwargs={'pk': 100})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_work_arrangement_update(self):
        """Testing work arrangement successful update view"""
        work_arrangement = WorkArrangement.objects.create(work='Printing', work_type='PT')
        self.assertEqual(work_arrangement.work_type, 'PT')
        data = {
            'work_type': 'FT'
        }
        data = json.dumps(data)
        url = reverse('work-arrangement-retrieve-update-delete', kwargs={'pk': work_arrangement.pk})
        response = self.client.patch(url, content_type='application/json', data=data)
        self.assertEqual(response.data['work_type'], 'FT')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_work_arrangement_update_invalid_work_type(self):
        """Testing work arrangement update view with invalid work type"""
        work_arrangement = WorkArrangement.objects.create(work='Data Analysis', work_type='FT')
        self.assertEqual(work_arrangement.work_type, 'FT')
        data = {
            'work_type': 'QT'
        }
        data = json.dumps(data)
        url = reverse('work-arrangement-retrieve-update-delete', kwargs={'pk': work_arrangement.pk})
        response = self.client.patch(url, content_type='application/json', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_work_arrangement(self):
        """Testing work arrangement successful delete view"""
        work_arrangement = WorkArrangement.objects.create(work='Data Analysis', work_type='FT')
        url = reverse('work-arrangement-retrieve-update-delete', kwargs={'pk': work_arrangement.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(WorkArrangement.objects.filter(id=work_arrangement.id).exists())

    def test_delete_work_arrangement_invalid_id(self):
        """Testing work arrangement delete view with invalid work type"""
        work_arrangement = WorkArrangement.objects.create(work='Python', work_type='FT')
        url = reverse('work-arrangement-retrieve-update-delete', kwargs={'pk': 100})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
