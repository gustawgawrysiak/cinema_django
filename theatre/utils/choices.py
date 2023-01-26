from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class FilmCategory(TextChoices):
    ACTION = "ACTION", _("Action")
    COMEDY = "COMEDY", _("Comedy")
    KIDS = "KIDS", _("For kids")
    THRILLER = "THRILLER", _("Thriller")
    ROMANCE = "ROMANCE", _("Romance")
    CRIME = "CRIME", _("Crime")
    SCI_FI = "SCIFI", _("Sci-Fi")
    MUSICAL = "MUSICAL", _("Musical")


class SeatCategory(TextChoices):
    NORMAL = "NORMAL", _("Normal")
    COMFORT = "COMFORT", _("Comfort")
    VIP = "VIP", _("Vip")


class EventCategory(TextChoices):
    FILM = "FILM", _("Film")
    PARTY = "PARTY", _("Party")
