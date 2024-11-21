from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Colecao

class ColecaoTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_colecao(self):
        data = {'nome': 'Minha Coleção', 'descricao': 'Descrição da coleção'}
        response = self.client.post('/api/colecoes/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_permission(self):
        another_user = User.objects.create_user(username='otheruser', password='otherpass')
        colecao = Colecao.objects.create(nome='Coleção de Teste', colecionador=self.user)
        self.client.force_authenticate(user=another_user)
        response = self.client.put(f'/api/colecoes/{colecao.id}/', {'nome': 'Novo Nome'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)