import uuid

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Analytical


class AnalyticalAPITests(APITestCase):

    def setUp(self):
        # Создаем несколько объектов для тестов
        self.analytical1 = Analytical.objects.create(name="Analytical 1")
        self.analytical2 = Analytical.objects.create(name="Analytical 2")
        self.list_url = reverse('analytical-list-create')
        self.detail_url = lambda pk: reverse('analytical-detail', args=[pk])

    def test_get_all_analyticals(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], self.analytical1.name)
        self.assertEqual(response.data[1]['name'], self.analytical2.name)

    def test_create_analytical(self):
        data = {"name": "Analytical 3"}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Analytical.objects.count(), 3)
        self.assertEqual(response.data['name'], data['name'])

    def test_get_single_analytical(self):
        response = self.client.get(self.detail_url(self.analytical1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.analytical1.name)

    def test_update_analytical(self):
        data = {"name": "Updated Analytical"}
        response = self.client.put(self.detail_url(self.analytical1.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.analytical1.refresh_from_db()
        self.assertEqual(self.analytical1.name, data['name'])

    def test_delete_analytical(self):
        response = self.client.delete(self.detail_url(self.analytical1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Analytical.objects.count(), 1)

    def test_create_analytical_with_invalid_data(self):
        data = {"name": ""}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Analytical.objects.count(), 2)

    def test_update_non_existent_analytical(self):
        non_existent_id = uuid.uuid4()
        data = {"name": "Updated Non-Existent Analytical"}
        response = self.client.put(self.detail_url(non_existent_id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_non_existent_analytical(self):
        non_existent_id = uuid.uuid4()
        response = self.client.delete(self.detail_url(non_existent_id))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

# Create your tests here.
