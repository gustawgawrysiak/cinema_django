from rest_framework import serializers
from theatre.models import Event, Hall, Film
from theatre.utils.choices import EventCategory
from theatre.utils.constants import BREAK_INTERVAL
from typing import Dict
import datetime


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class AddEventSerializer(serializers.Serializer):
    hall_id = serializers.SlugRelatedField(
        slug_field='id',
        queryset=Hall.objects.all()
    )
    film_id = serializers.SlugRelatedField(
        slug_field='id',
        queryset=Film.objects.all()
    )
    date_start = serializers.DateTimeField()
    category = serializers.ChoiceField(choices=EventCategory.choices)

    def create(self, validated_data: Dict) -> Event:
        date_start = validated_data["date_start"]
        date_end = validated_data["film_id"].length + BREAK_INTERVAL
        event = Event(
            hall_id=validated_data["hall_id"],
            film_id=validated_data["film_id"],
            date_start=date_start,
            date_end=date_start + datetime.timedelta(minutes=date_end),
            category=validated_data["category"]
        )
        event.save()
        return event

    def save(self, **kwargs):
        super().save(**kwargs)

    def update(self, instance, validated_data):
        pass
