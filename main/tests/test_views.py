from django.test import TestCase, Client


class APIViewTests(TestCase):

    def test_get_valid_data(self):
        client = Client()
        response = client.get(
            "/fib",
            {
                "n": 100,
            },
        )
        self.assertEqual(200, response.status_code)

    def test_get_empty_data(self):
        client = Client()
        response = client.get(
            "/fib",
        )
        self.assertEqual(400, response.status_code)

    def test_get_invalid_data(self):
        client = Client()
        response = client.get(
            "/fib",
            {
                "n": "あ",
            },
        )
        self.assertEqual(400, response.status_code)
