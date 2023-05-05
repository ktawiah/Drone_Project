from django.shortcuts import render
from rest_framework import generics
from .models import Drone, DroneCategory, Pilot
from .serializers import DroneSerializer, DroneCategorySerializer, PilotSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.


class ApiRootView(generics.GenericAPIView):
    def get(self, request, format=None):
        return Response(
            {
                "drones": reverse(
                    "drone_app:drone-list", request=request, format=format
                ),
                "drone categories": reverse(
                    "drone_app:drone-category-list", request=request, format=format
                ),
                "pilots": reverse(
                    "drone_app:pilot-list", request=request, format=format
                ),
            }
        )


class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer


class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer


class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
