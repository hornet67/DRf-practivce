# api/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from api.models import Book
from datetime import date

class Command(BaseCommand):
    def handle(self, *args, **options):
        Book.objects.all().delete()
        
        books = [
            Book(title="Django for APIs", author="William S. Vincent", price=29.99, published_date=date(2023, 1, 15), in_stock=True),
            Book(title="Python Crash Course", author="Eric Matthes", price=39.99, published_date=date(2022, 5, 20), in_stock=True),
            Book(title="RESTful Web APIs", author="Leonard Richardson", price=49.99, published_date=date(2021, 11, 10), in_stock=False),
        ]
        
        for book in books:
            book.save()
        
        self.stdout.write(self.style.SUCCESS(f"Added {len(books)} books"))