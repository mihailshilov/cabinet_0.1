from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from newcars.models import NewCar
from newcars.serializers import NewCarSerializer


class NewCarsApiTestCase(APITestCase):
    def setUp(self):
        self.car_1 = NewCar.objects.create(vin='123456S60', con='65498787', price=1115000.00, img='/ty/', engine='rtrt',
                                      fuel_type='disel', compl='comfort', model='S90', link='/lnk/')
        self.car_2 = NewCar.objects.create(vin='823456', con='85498787', price=1235000.00, img='/ty/', engine='rtrt',
                                      fuel_type='disel', compl='comfort', model='S60', link='/lnk/2')

    def test_get(self):

        url = reverse('newcar-list')
        serialized_data = NewCarSerializer([self.car_1, self.car_2], many=True).data
        response = self.client.get(url)

        print(serialized_data)
        print(response.data)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)

    def test_get_search(self):

        url = reverse('newcar-list')
        serialized_data = NewCarSerializer([self.car_1, self.car_2], many=True).data
        response = self.client.get(url, data={'search': 'S60'})

        print(serialized_data)
        print(response.data)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)


