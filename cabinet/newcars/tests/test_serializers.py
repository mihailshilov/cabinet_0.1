# from django.test import TestCase
from unittest import TestCase

from newcars.models import NewCar
from newcars.serializers import NewCarSerializer


class NewCarSerializerTestCase(TestCase):
    def test_ok(self):

        car_1 = NewCar.objects.create(vin='123456', con='65498787', price=1100000.00, img='/ty/', engine='rtrt',
                                      fuel_type='disel', compl='comfort', model='XC90', link='/lnk/')
        car_2 = NewCar.objects.create(vin='723456', con='75498787', price=1100000.00, img='/ty/', engine='rtrt',
                                      fuel_type='disel', compl='comfort', model='XC90', link='/lnk/')

        data = NewCarSerializer([car_1, car_2], many=True).data

        expected_data = [
            {
                'id': car_1.id,
                'vin': '123456',
                'con': '65498787',
                'price': 1100000.00,
                'img': '/ty/',
                'engine': 'rtrt',
                'fuel_type': 'disel',
                'compl': 'comfort',
                'model': 'XC90',
                'link': '/lnk/',
            },
            {
                'id': car_2.id,
                'vin': '723456',
                'con': '75498787',
                'price': 1100000.00,
                'img': '/ty/',
                'engine': 'rtrt',
                'fuel_type': 'disel',
                'compl': 'comfort',
                'model': 'XC90',
                'link': '/lnk/',
            }
        ]

        print(expected_data, '\n', data)

        self.assertEqual(expected_data, data)
