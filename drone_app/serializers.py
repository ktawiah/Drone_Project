from rest_framework import serializers
from .models import Drone, DroneCategory, Pilot


class DroneCategorySerializer(serializers.ModelSerializer):
    drones = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = DroneCategory
        fields = ("id", "name", "drones")


class DroneSerializer(serializers.ModelSerializer):
    drone_category = serializers.SlugRelatedField(
        queryset=DroneCategory.objects.all(), slug_field="name"
    )
    url = serializers.HyperlinkedIdentityField(view_name="drone:drone-detail")

    class Meta:
        model = Drone
        fields = (
            "name",
            "drone_category",
            "manufacturing_date",
            "has_it_competed",
            "inserted_timestamp",
            "url",
        )


class PilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilot
        fields = ("id", "name", "gender", "races_count", "inserted_timestamp")
