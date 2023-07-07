from django.test import TestCase

from theatre.api.serializers import AddSeatSerializer
from theatre.models import Seat, Hall
from theatre.utils import SeatCategory


class FilmTestCase(TestCase):
    @classmethod
    def setUp(cls) -> None:
        hall1 = Hall.objects.create(**{
            "capacity": 100,
            "description": 'Sala nr 1',
            "max_row": 'G',
            "max_col": '25'
        })

    def test_create_seats_from_serializer(self):
        seat = {
            "hall_id": 1,
            "seat_category": SeatCategory.VIP,
            "place": "A32",
            "description": "Miejsce przy wejściu",
        }
        add_seat_serializer = AddSeatSerializer(data=seat)
        add_seat_serializer.is_valid()
        add_seat_serializer.save()

        seat = Seat.objects.first()

        self.assertEqual(seat.seat_category, "VIP")
        self.assertEqual(seat.place, 'A32')
        self.assertEqual(seat.description, "Miejsce przy wejściu")

        self.assertNotEqual(seat.seat_category, "COMFORT")
        self.assertNotEqual(seat.place, '33')
        self.assertNotEqual(seat.description, "NIC")

        def create_seat(self):
            seat_kwargs= {"hall_id": 5,
                    "seat_category": SeatCategory.COMFORT,
                    "place": "A32",
                    "description":"Nie wiem" }
            seat2 = Seat.objects.create(**seat_kwargs)

            self.assertEqual(seat2.hall_id, '5')
            self.assertEqual(seat2.seat_category, SeatCategory.COMFORT)
            self.assertEqual(seat2.place, '40')
            self.assertEqual(seat2.description, "Nie wiem")

            self.assertNotEqual(seat2.hall_id, '7')
            self.assertNotEqual(seat2.seat_category, SeatCategory.VIP)
            self.assertNotEqual(seat2.place, '41')
            self.assertNotEqual(seat2.description, "Nie")
