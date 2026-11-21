
from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path("", views.home, name="home"),
    path("ecole/", views.ecole, name="ecole"),
    path("pedagogie/", views.pedagogie, name="pedagogie"),
    path("vie/", views.vie, name="vie"),
    path("admissions/", views.admissions, name="admissions"),
    path("actualites/", views.actualites, name="actualites"),
    path("calendrier/", views.calendrier, name="calendrier"),
    path("contact/", views.contact, name="contact"),
    path("connexion/", views.connexion, name="connexion"),
    path("admissions/preinscription/", views.preinscription, name="preinscription"),
    path("visite/", views.visite, name="visite"),
]
