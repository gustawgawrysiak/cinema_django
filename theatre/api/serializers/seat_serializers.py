from rest_framework import serializers
from theatre.models import Seat, Hall
from typing import Dict

from theatre.utils import SeatCategory


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class AddSeatSerializer(serializers.Serializer):
    hall_id = serializers.SlugRelatedField('id', queryset=Hall.objects.all())
    seat_category = serializers.ChoiceField(choices=SeatCategory.choices)
    place = serializers.CharField()
    description = serializers.CharField()

    def create(self, validated_data: Dict) -> Seat:
        seat = Seat(
            hall_id=validated_data["hall_id"],
            seat_category=validated_data["seat_category"],
            place=validated_data["place"],
            description=validated_data["description"]
        )
        seat.save()
        return seat

    def save(self, **kwargs):
        super().save(**kwargs)

    def update(self, instance, validated_data):
        pass
