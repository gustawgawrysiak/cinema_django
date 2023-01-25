from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from theatre.models import Hall
from django.db.models import QuerySet
from typing import Any, Type
from ..serializers import AddHallSerializer, HallSerializer


class HallViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericViewSet):
    permission_classes = [IsAuthenticated, ]
    filter_backends = [SearchFilter, ]
    # filterset_class =
    queryset = Hall.objects.all()
    search_fields = '__all__'

    def get_serializer_class(self) -> Type:
        return {
            'list': HallSerializer,
            'create': AddHallSerializer,
            'retrieve': HallSerializer
        }[self.action]

    def get_queryset(self) -> QuerySet:
        qs = super().get_queryset()
        return qs

    def create(self, request, *args: Any, **kwargs: Any) -> Response:
        serializer: AddHallSerializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        try:
            hall = self.perform_create(serializer)
        except Exception as e:
            return Response(
                data={"message": "failed to create"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        obj_serializer = HallSerializer(hall)
        return Response(
            data=obj_serializer.data,
            status=status.HTTP_201_CREATED
        )

    def retrieve(self, request: Request, *args: Any, **kwargs: Any):
        return super().retrieve(request, *args, **kwargs)

    def perform_create(self, serializer) -> Hall:
        hall: Hall = serializer.save()
        return hall
