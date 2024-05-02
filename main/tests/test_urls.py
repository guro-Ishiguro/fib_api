from django.test import TestCase
from django.urls import resolve
from ..views import FibViewSet


class TestUrls(TestCase):

    def test_post_index_url(self):
        view = resolve("/fib")
        self.assertEqual(view.func.view_class, FibViewSet)
