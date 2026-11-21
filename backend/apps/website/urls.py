from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path("", views.home, name="home"),

    # École
    path("ecole/", views.ecole, name="ecole"),
    path("ecole/histoire/", views.histoire, name="histoire"),
    path("ecole/mission/", views.mission, name="mission"),
    path("ecole/espaces/", views.espaces, name="espaces"),

    # Pédagogie
    path("pedagogie/", views.pedagogie, name="pedagogie"),
    path("pedagogie/approche/", views.approche, name="approche"),
    path("pedagogie/prescolaire/", views.cycle, {"nom": "prescolaire", "titre": "Préscolaire"}, name="prescolaire"),
    path("pedagogie/primaire/", views.cycle, {"nom": "primaire", "titre": "Primaire"}, name="primaire"),
    path("pedagogie/college/", views.cycle, {"nom": "college", "titre": "Collège"}, name="college"),

    # Vie scolaire
    path("vie/", views.vie, name="vie"),
    path("vie/activites/", views.activites, name="activites"),
    path("vie/robotique/", views.robotique, name="robotique"),
    path("vie/sorties/", views.sorties, name="sorties"),

    # Admissions
    path("admissions/", views.admissions, name="admissions"),
    path("admissions/preinscription/", views.preinscription, name="preinscription"),
    path("admissions/dossier/", views.dossier, name="dossier"),
    path("admissions/visite/", views.visite, name="visite"),

    # Informations
    path("actualites/", views.actualites, name="actualites"),
    path("calendrier/", views.calendrier, name="calendrier"),
    path("contact/", views.contact, name="contact"),
    path("connexion/", views.connexion, name="connexion"),
]