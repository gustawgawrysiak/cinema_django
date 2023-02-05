from django.test import TestCase

from theatre.api.serializers import AddHallSerializer
from theatre.models import Hall


class HallTestCase(TestCase):
    @classmethod
    def setUp(cls) -> None:
        pass

    def test_create_hall(self):
        add_hall_serializer = AddHallSerializer()
        hall_dict = {
            "capacity": 100,
            "description": 'Sala nr 1',
            "max_row": 'G',
            "max_col": '25'
        }
        hall1 = add_hall_serializer.create(hall_dict)
        self.assertEqual(hall1.capacity, 100)
        self.assertEqual(hall1.description, 'Sala nr 1')
        self.assertEqual(hall1.max_row, 'G')
        self.assertEqual(hall1.max_col, '25')
        self.assertNotEqual(hall1.capacity, -100)
        self.assertNotEqual(hall1.description, 'sala nr 1')
        self.assertNotEqual(hall1.max_row, 'Z')
        self.assertNotEqual(hall1.max_col, '125')

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

        self.assertEqual(Hall.objects.count(), 2)
