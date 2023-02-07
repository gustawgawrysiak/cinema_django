from django.test import TestCase
from theatre.models import Film


class FilmTestCase(TestCase):

    def setUp(self):
        e = Film(category="ACTION",
                 length=1,
                title='sss',
                 description='aaaa')
