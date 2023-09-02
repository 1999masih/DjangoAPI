from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@mail.com",
            password="123",
        )

        cls.post = Post.objects.create(
            author = cls.user,
            title = "A good title",
            body = "Nice Body!"
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice Body!")
        self.assertEqual(str(self.post), "A good title")

