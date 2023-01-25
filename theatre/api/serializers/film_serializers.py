from typing import Dict

from rest_framework import serializers
from theatre.models import Film


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class AddFilmSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    length = serializers.CharField(required=True)
    category = serializers.CharField(required=True)

    def create(self, validated_data: Dict) -> Film:
        film = Film(
            title=validated_data["title"],
            description=validated_data["description"],
            length=validated_data["length"],
            category=validated_data["category"]
        )
        film.save()
        return film

    def save(self, **kwargs):
        super().save(**kwargs)

    def update(self, instance, validated_data):
        pass
