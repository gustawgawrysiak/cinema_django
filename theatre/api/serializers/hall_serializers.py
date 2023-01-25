from rest_framework import serializers
from theatre.models import Hall
from typing import Dict


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'


class AddHallSerializer(serializers.Serializer):
    capacity = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    max_row = serializers.CharField(required=True)
    max_col = serializers.CharField(required=True)

    def create(self, validated_data: Dict) -> Hall:
        hall = Hall(
            capacity=validated_data["capacity"],
            description=validated_data["description"],
            max_row=validated_data["max_row"],
            max_col=validated_data["max_col"]
        )
        hall.save()
        return hall

    def save(self, **kwargs) -> None:
        super().save(**kwargs)

    def update(self, instance, validated_data):
        pass
