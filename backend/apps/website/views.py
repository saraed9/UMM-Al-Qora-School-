
from django.shortcuts import render


def home(request):
    return render(request, "website/home.html")


def ecole(request):
    return render(request, "website/page.html", {
        "title": "Notre école",
        "subtitle": "Une école moderne où chaque enfant a sa place.",
        "description": "Découvrez UMM ALQORA d’EXCELLENCE, son histoire, sa mission, ses valeurs et ses espaces.",
        "sections": [
            {
                "title": "Notre mission",
                "text": "Offrir aux enfants une éducation exigeante, bienveillante et adaptée à leurs besoins."
            },
            {
                "title": "Nos valeurs",
                "text": "Excellence, respect, accompagnement individualisé et ouverture sur le monde."
            },
            {
                "title": "Nos locaux",
                "text": "Des salles de classe, une bibliothèque, des laboratoires scientifiques et des espaces de vie."
            },
        ],
    })


def pedagogie(request):
    return render(request, "website/page.html", {
        "title": "Notre pédagogie",
        "subtitle": "Une pédagogie exigeante, trilingue et bienveillante.",
        "description": "Notre approche pédagogique accompagne chaque enfant dans son développement.",
        "sections": [
            {
                "title": "Préscolaire",
                "text": "Un environnement adapté à la découverte, au jeu et aux premiers apprentissages."
            },
            {
                "title": "Primaire",
                "text": "Des bases solides en arabe, français, anglais, mathématiques et sciences."
            },
            {
                "title": "Collège",
                "text": "Un cycle exigeant pour développer l'autonomie et préparer la suite du parcours scolaire."
            },
            {
                "title": "Trois langues",
                "text": "Arabe, français et anglais au cœur de notre approche trilingue."
            },
        ],
    })


def vie(request):
    return render(request, "website/page.html", {
        "title": "La vie à l'école",
        "subtitle": "Une école où chaque enfant a sa place.",
        "description": "Au-delà de la classe, les élèves découvrent, créent et développent leurs passions.",
        "sections": [
            {
                "title": "Sport",
                "text": "Des activités sportives pour bouger et apprendre à jouer ensemble."
            },
            {
                "title": "Théâtre",
                "text": "Un atelier pour développer l'expression et la confiance en soi."
            },
            {
                "title": "Robotique et informatique",
                "text": "Construire, programmer et créer avec le numérique."
            },
            {
                "title": "Sorties éducatives",
                "text": "Des visites pour apprendre également en dehors de l'école."
            },
        ],
    })


def admissions(request):
    return render(request, "website/page.html", {
        "title": "Admissions",
        "subtitle": "Rejoignez UMM ALQORA d’EXCELLENCE.",
        "description": "Retrouvez les informations nécessaires pour préparer l'inscription de votre enfant.",
        "sections": [
            {
                "title": "Préscolaire",
                "text": "Découvrez notre parcours préscolaire et son approche pédagogique."
            },
            {
                "title": "Primaire",
                "text": "Découvrez notre programme et notre accompagnement des élèves."
            },
            {
                "title": "Collège",
                "text": "Découvrez notre organisation et notre approche pour le cycle collège."
            },
        ],
    })


def actualites(request):
    return render(request, "website/page.html", {
        "title": "Actualités",
        "subtitle": "Les nouvelles de notre école.",
        "description": "Retrouvez les actualités et les événements d'UMM ALQORA d’EXCELLENCE.",
        "sections": [
            {
                "title": "Journées portes ouvertes",
                "text": "Les informations concernant les prochaines journées portes ouvertes seront publiées ici."
            },
            {
                "title": "Rentrée scolaire 2027",
                "text": "Les informations relatives à la rentrée de septembre 2027 seront communiquées prochainement."
            },
        ],
    })


def calendrier(request):
    return render(request, "website/page.html", {
        "title": "Calendrier scolaire",
        "subtitle": "Les grandes dates de l'année scolaire 2027-2028.",
        "description": "Retrouvez ici les dates de rentrée, les journées portes ouvertes, les vacances et les événements de l'école.",
        "sections": [
            {
                "title": "Rentrée scolaire",
                "text": "Date à confirmer."
            },
            {
                "title": "Journées portes ouvertes",
                "text": "Dates à communiquer."
            },
            {
                "title": "Vacances scolaires",
                "text": "Calendrier à confirmer par l'établissement."
            },
        ],
    })


def contact(request):
    return render(request, "website/contact.html")


def connexion(request):
    return render(request, "website/connexion.html")


def preinscription(request):
    return render(request, "website/preinscription.html")


def visite(request):
    return render(request, "website/visite.html")
