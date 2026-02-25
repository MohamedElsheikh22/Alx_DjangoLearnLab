from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
# Create your views here.

#ListAPIView: retrieve all books (public access)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

#RetrieveAPIView
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

#CreateAPIView: authenticated users only 
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

#UpdateAPIView: authenticated users only
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

#DestroyAPIView: authenticated users only
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
