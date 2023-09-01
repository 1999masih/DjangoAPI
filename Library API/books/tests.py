from django.test import TestCase
from django.urls import reverse

from .models import Book

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title = "good title",
            subtitle = "good subtitle",
            author = "masih",
            isbn = "123",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "good title")
        self.assertEqual(self.book.subtitle, "good subtitle")
        self.assertEqual(self.book.author, "masih")
        self.assertEqual(self.book.isbn, "123")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "good subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")
        
