from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='123456'
        )
        self.author = Author.objects.create(name='Mohamed')
        self.book = Book.objects.create(
            title='Django DRF',
            publication_year=2024,
            author=self.author
        )
    
    def test_get_books_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data)>0)

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='123456')
        url = reverse('book-create')
        data ={
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.id

        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_update_book(self):
        self.client.login(username='testuser', password='123456')
        url = reverse('book-update', args=[self.book.id])
        data = {
            'title': 'New Book',
            'publication_year': 2020,
            'author': self.author.id

        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_book(self):
        self.client.login(username='testuser', password='123456')
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)