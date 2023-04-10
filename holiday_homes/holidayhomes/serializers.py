from rest_framework import serializers

from .models import *


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'


class HolidayHomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = HolidayHome
        fields = '__all__'


class HomeDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeDetail
        fields = '__all__'
