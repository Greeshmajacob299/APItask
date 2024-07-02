from .models import *
from rest_framework import serializers


class TourismSerializers(serializers.ModelSerializer):
    dest_image = serializers.ImageField(required=False)

    class Meta:
        model = Destination
        fields = '__all__'
