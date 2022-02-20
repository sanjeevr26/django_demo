from rest_framework import serializers
from .models import Hotels, Guest


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = ['id','name', 'price']


class GuestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'guest_name']