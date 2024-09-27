from django.test import TestCase

from theatre.api.serializers import AddHallSerializer
from theatre.models import Hall


class HallTestCase(TestCase):
    @classmethod
    def setUp(cls) -> None:
        pass

    def test_create_hall_from_serializer(self):
        hall_dict = {
            "capacity": 100,
            "description": 'Sala nr 1',
            "max_row": 'G',
            "max_col": '25'
        }
        add_hall_serializer = AddHallSerializer(data=hall_dict)
        add_hall_serializer.is_valid()
        add_hall_serializer.save()
        hall1 = Hall.objects.first()
        self.assertEqual(hall1.capacity, 100)
        self.assertEqual(hall1.description, 'Sala nr 1')
        self.assertEqual(hall1.max_row, 'G')
        self.assertEqual(hall1.max_col, '25')
        self.assertNotEqual(hall1.capacity, -100)
        self.assertNotEqual(hall1.description, 'sala nr 1')
        self.assertNotEqual(hall1.max_row, 'Z')
        self.assertNotEqual(hall1.max_col, '125')

    def test_create_hall(self):
        hall2 = Hall.objects.create(capacity=250,
                                    description="Sala nr 2",
                                    max_row="M",
                                    max_col="35")
        self.assertEqual(hall2.capacity, 250)
        self.assertEqual(hall2.description, 'Sala nr 2')
        self.assertEqual(hall2.max_row, 'M')
        self.assertEqual(hall2.max_col, '35')
        self.assertNotEqual(hall2.capacity, 100)
        self.assertNotEqual(hall2.description, 'Sala nr 1')
        self.assertNotEqual(hall2.max_row, 'A')
        self.assertNotEqual(hall2.max_col, '1')
