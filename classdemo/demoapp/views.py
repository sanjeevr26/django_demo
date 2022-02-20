from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import HotelSerializers, GuestSerializers
from rest_framework import generics
from rest_framework import filters
from .models import Hotels, Guest
# Create your views here.


def home(request):
    return HttpResponse("<h1> HELLO WORLD </h1>")


@api_view(['GET', 'POST'])
def Hotels_list(request):
    if request.method == 'GET':
        hotels_list = Hotels.objects.all()
        hotelSerializer = HotelSerializers(hotels_list, many=True)
        return Response(hotelSerializer.data)
    if request.method == 'POST':
        hotel_request = request.data
        serialize_request_data = HotelSerializers(data=hotel_request)
        if serialize_request_data.is_valid():
            serialize_request_data.save()

        return Response({"Message": "Added Successfully"})


@api_view(['GET', 'POST'])
def Hotels_detail(request,pk):
    if request.method == 'GET':
        hotels_list = Hotels.objects.get(id=pk)
        hotelSerializer = HotelSerializers(hotels_list, many=False)
        return Response(hotelSerializer.data)


class get_generics_list(generics.ListCreateAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelSerializers

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


@api_view(['GET'])
def guest_list(request):
    if request.method == "GET":
        guest_list = Guest.objects.all()
        guest_serializer = GuestSerializers(guest_list, many=True)
        print(guest_serializer.data)
        return Response(guest_serializer.data)