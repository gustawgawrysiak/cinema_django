from django.urls import path, include

from rest_framework import routers

from theatre.api import views

theatre_router = routers.SimpleRouter()

# root /api/v1/theatre

theatre_router.register(
    prefix=r'film',
    viewset=views.FilmViewSet,
    basename='theatre'
)
theatre_router.register(
    prefix=r'hall',
    viewset=views.HallViewSet,
    basename='theatre'
)
theatre_router.register(
    prefix=r'seat',
    viewset=views.SeatViewSet,
    basename='theatre'
)
theatre_router.register(
    prefix=r'event',
    viewset=views.EventViewSet,
    basename='theatre'
)
urlpatterns = [] + theatre_router.urls
