from rest_framework import generics, permissions  # ← Add 'permissions'
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_permissions(self):
        if self.request.method == 'POST':
            # Only logged-in users can create
            return [permissions.IsAuthenticated()]
        # Anyone can view (GET)
        return [permissions.AllowAny()]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_permissions(self):
        if self.request.method == 'DELETE':
            # Only admin can delete
            return [permissions.IsAdminUser()]
        elif self.request.method in ['PUT', 'PATCH']:
            # Only logged-in users can update
            return [permissions.IsAuthenticated()]
        # Anyone can view (GET)
        return [permissions.AllowAny()]