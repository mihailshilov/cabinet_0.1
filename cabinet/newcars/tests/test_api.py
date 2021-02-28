from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from newcars.models import NewCar
from newcars.serializers import NewCarSerializer


class NewCarsApiTestCase(APITestCase):
    def test_get(self):
        car_1 = NewCar.objects.create(vin='123456', con='65498787', price=1100000.00, img='/ty/', engine='rtrt', fuel_type='disel', compl='comfort', model='XC90', link='/lnk/')
        car_2 = NewCar.objects.create(vin='723456', con='75498787', price=1100000.00, img='/ty/', engine='rtrt', fuel_type='disel', compl='comfort', model='XC90', link='/lnk/')
        url = reverse('newcar-list')
        serialized_data = NewCarSerializer([car_1, car_2], many=True).data
        response = self.client.get(url)

        print(serialized_data)
        print(response.data)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)


