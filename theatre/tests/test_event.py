from django.test import TestCase
import datetime
from theatre.api.serializers import AddEventSerializer
from theatre.models import Event, Hall, Film
from theatre.utils import FilmCategory
from theatre.utils.choices import EventCategory


class FilmTestCase(TestCase):
    @classmethod
    def setUp(cls) -> None:
        hall1 = Hall.objects.create(**{
            "capacity": 100,
            "description": 'Sala nr 1',
            "max_row": 'G',
            "max_col": '25'
        })

        film1= Film.objects.create(**{
                "title": 'SpiderMan',
                "description": 'film o spider manie',
                "length": 150,
                "category": 'ACTION'
        })

    def test_create_event(self):
        event_dict = {
            "hall_id": 1,
            "film_id": 1,
            "date_start": datetime.datetime(2022, 11, 21),
            "date_end": datetime.datetime(2022, 11, 29),
            "category": EventCategory.FILM

        }
        add_event_serializer = AddEventSerializer(data=event_dict)
        add_event_serializer.is_valid()
        add_event_serializer.save()

        event = Event.objects.first()

        self.assertEqual(event.date_start, datetime.datetime(2022, 11, 21, 0, 0, tzinfo=datetime.timezone.utc))
        self.assertEqual(event.date_end, datetime.datetime(2022, 11, 21, 2, 50,  tzinfo=datetime.timezone.utc))
        self.assertEqual(event.category, EventCategory.FILM)

        self.assertNotEqual(event.date_start, datetime.datetime(2022, 11, 22, tzinfo=datetime.timezone.utc))
        self.assertNotEqual(event.date_end, datetime.datetime(2022, 11, 30, tzinfo=datetime.timezone.utc))
        self.assertNotEqual(event.category, EventCategory.PARTY)

        event2 = {
                "hall_id": 1,
                "film_id": 1,
                "date_start": datetime.datetime(2022, 12, 12),
                "date_end": datetime.datetime(2022, 12, 30),
                "category": 'FILM'}

        add_event_serializer = AddEventSerializer(data=event2)
        add_event_serializer.is_valid(raise_exception=True)
        add_event_serializer.save()

        event2 = Event.objects.first()

        self.assertEqual(event2.date_start, datetime.datetime(2022, 11, 21, 0, 0, tzinfo=datetime.timezone.utc))
        self.assertEqual(event2.date_end, datetime.datetime(2022, 11, 21, 2, 50, tzinfo=datetime.timezone.utc))
        self.assertEqual(event2.category, EventCategory.FILM)

        self.assertNotEqual(event2.date_start, datetime.datetime(2022, 11, 22, tzinfo=datetime.timezone.utc))
        self.assertNotEqual(event2.date_end, datetime.datetime(2022, 11, 30, tzinfo=datetime.timezone.utc))
        self.assertNotEqual(event2.category, EventCategory.PARTY)
