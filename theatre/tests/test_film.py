from django.test import TestCase

from theatre.api.serializers import AddFilmSerializer
from theatre.models import Film
from theatre.utils.choices import FilmCategory


class FilmTestCase(TestCase):
    @classmethod
    def setUp(cls) -> None:
        pass

    def test_create_film(self):
        add_film_serializer = AddFilmSerializer()
        film_dict = {
            "title": 'SpiderMan',
            "description": 'film o spider manie',
            "length": 150,
            "category": 'ACTION'
        }
        film1 = add_film_serializer.create(film_dict)
        self.assertEqual(film1.title, 'SpiderMan')
        self.assertEqual(film1.description, 'film o spider manie')
        self.assertEqual(film1.length, 150)
        self.assertEqual(film1.category, FilmCategory.ACTION)
        self.assertNotEqual(film1.title, 'SpiderMan2')
        self.assertNotEqual(film1.description, 'drugi film o spider manie')
        self.assertNotEqual(film1.length, 120)
        self.assertNotEqual(film1.category, 'KIDS')

        film2 = Film.objects.create(title="SpiderMan2",
                                    description="drugi film o spider manie",
                                    length=120,
                                    category=FilmCategory.ACTION)
        self.assertEqual(film2.title, 'SpiderMan2')
        self.assertEqual(film2.description, 'drugi film o spider manie')
        self.assertEqual(film2.length, 120)
        self.assertEqual(film2.category, FilmCategory.ACTION)
        self.assertNotEqual(film2.title, 'SpiderMan')
        self.assertNotEqual(film2.description, 'film o spider manie')
        self.assertNotEqual(film2.length, 150)
        self.assertNotEqual(film2.category, FilmCategory.CRIME)

        self.assertEqual(Film.objects.count(), 2)
