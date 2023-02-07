from typing import Dict

from rest_framework import serializers
from tickets.models import Ticket
from theatre.models import Film



class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class AddTicketSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    length = serializers.CharField(required=True)

    def create(self, validated_data: Dict) -> Ticket:
        ticket = Ticket(
            title = ticket.validate_title(validated_data["title"]),
            description=validated_data["description"],
            length=validated_data["length"]
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
