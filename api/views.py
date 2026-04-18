from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
# Create your views here.

class BookListCreateView(generics.ListCreateAPIView):
    data = Book.objects.all()
    serializer_class = BookSerializer   


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    data = Book.objects.all()
    serializer_class = BookSerializer