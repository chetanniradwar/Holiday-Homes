from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import OwnerSerializer, RoomSerializer, HolidayHomeSerializer, HomeDetailSerializer


class HolidayHomeViewSet(viewsets.ModelViewSet):
    queryset = HolidayHome.objects.all()
    serializer_class = HolidayHomeSerializer

    @action(methods=['get'], detail=True)
    def retrieve_with_room_details(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            home_obj = HolidayHome.objects.get(id=pk)
        except Exception:
            return Response({"error": "holiday home does not exists"}, status=status.HTTP_400_BAD_REQUEST)

        rooms = Room.objects.filter(holiday_home=home_obj.id)

        home_data = HolidayHomeSerializer(home_obj).data

        room_data = RoomSerializer(rooms, many=True).data

        home_data.update({"room_data": room_data})

        return Response(home_data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def retrieve_with_availability_details(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            home_obj = HolidayHome.objects.get(id=pk)
        except Exception:
            return Response({"error": "holiday home does not exists"}, status=status.HTTP_400_BAD_REQUEST)

        home_details = HomeDetail.objects.filter(holiday_home=home_obj.id)

        home_data = HolidayHomeSerializer(home_obj).data

        home_details_data = HomeDetailSerializer(home_details, many=True).data

        home_data.update({"availability_data": home_details_data})

        return Response(home_data, status=status.HTTP_200_OK)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

    @action(methods=['get'], detail=True)
    def retrieve_with_holiday_homes_data(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            owner_obj = Owner.objects.get(id=pk)
        except Exception:
            return Response({"error": "owner does not exists"}, status=status.HTTP_400_BAD_REQUEST)

        owner_holiday_homes = HolidayHome.objects.filter(owners=owner_obj.id)

        owner_data = OwnerSerializer(owner_obj).data

        owner_holiday_homes_data = HolidayHomeSerializer(owner_holiday_homes, many=True).data

        owner_data.update({"holiday_homes_data": owner_holiday_homes_data})

        return Response(owner_data, status=status.HTTP_200_OK)


class HomeDetailViewSet(viewsets.ModelViewSet):
    queryset = HomeDetail.objects.all()
    serializer_class = HomeDetailSerializer
