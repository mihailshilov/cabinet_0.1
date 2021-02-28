from rest_framework.serializers import ModelSerializer

from newcars.models import NewCar


class NewCarSerializer(ModelSerializer):
    class Meta:
        model = NewCar
        fields = '__all__'
