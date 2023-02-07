from rest_framework import routers

from tickets.api import views

tickets_router = routers.SimpleRouter()

# root /api/v1/tickets

tickets_router.register(
    prefix=r'ticket',
    viewset=views.TicketViewSet,
    basename='tickets'
)

urlpatterns = [] + tickets_router.urls
