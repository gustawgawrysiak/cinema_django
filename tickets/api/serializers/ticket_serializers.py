from typing import Dict

from rest_framework import serializers
from tickets.models import Ticket
from theatre.models import Film, Event, Seat


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class AddTicketSerializer(serializers.Serializer):
    event_id = serializers.SlugRelatedField(slug_field='id',
                                            queryset=Event.objects.all())
    description = serializers.CharField(required=False)
    seat_id = serializers.SlugRelatedField(slug_field='id',
                                           queryset=Seat.objects.all())

    def create(self, validated_data: Dict) -> Ticket:
        ticket = Ticket(
            event_id=validated_data["event_id"],
            description=validated_data["description"],
            seat_id=validated_data["seat_id"]
        )
        ticket.save()
        return ticket

    def validate_title(self,data):
        film = Film.objects.get(title=data)
        if not film.title:
            raise serializers.ValidationError("Nie ma takiego filmu.")
        return data

    def save(self, **kwargs):
        super().save(**kwargs)

    def update(self, instance, validated_data):
        pass
