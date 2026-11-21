from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm, PreinscriptionForm, VisiteForm


def home(request):
    return render(request, "website/home.html")


def page(request, title, subtitle, description, sections):
    return render(request, "website/page.html", {
        "title": title,
        "subtitle": subtitle,
        "description": description,
        "sections": sections,
    })


def ecole(request):
    return page(
        request,
        "Notre école",
        "Une école moderne où chaque enfant a sa place.",
        "Découvrez UMM ALQORA d’EXCELLENCE, son histoire, sa mission et ses espaces.",
        [
            {
                "title": "Notre histoire",
                "text": "Découvrez l'histoire et le projet de notre établissement."
            },
            {
                "title": "Notre mission",
                "text": "Offrir aux enfants une éducation exigeante et bienveillante."
            },
            {
                "title": "Nos valeurs",
                "text": "Excellence, respect, autonomie et ouverture sur le monde."
            },
            {
                "title": "Nos espaces",
                "text": "Des espaces conçus pour apprendre, découvrir et s'épanouir."
            },
        ],
    )


def pedagogie(request):
    return page(
        request,
        "Notre pédagogie",
        "Apprendre, découvrir et progresser.",
        "Une approche pédagogique adaptée à chaque étape du développement de l'enfant.",
        [
            {
                "title": "Préscolaire",
                "text": "Découverte, jeu, langage et premiers apprentissages."
            },
            {
                "title": "Primaire",
                "text": "Acquisition des connaissances fondamentales et développement de l'autonomie."
            },
            {
                "title": "Collège",
                "text": "Approfondissement des connaissances et préparation à la poursuite des études."
            },
            {
                "title": "Notre approche",
                "text": "Un accompagnement pédagogique qui valorise la curiosité et la créativité."
            },
        ],
    )


def vie(request):
    return page(
        request,
        "La vie à l'école",
        "Apprendre aussi en dehors de la classe.",
        "Les activités contribuent au développement personnel et collectif des élèves.",
        [
            {
                "title": "Activités parascolaires",
                "text": "Des activités variées pour découvrir de nouvelles passions."
            },
            {
                "title": "Informatique et robotique",
                "text": "Découvrir le numérique, la logique et la programmation."
            },
            {
                "title": "Sorties éducatives",
                "text": "Des expériences pour découvrir le monde qui nous entoure."
            },
            {
                "title": "Sport et culture",
                "text": "Développer l'esprit d'équipe, la créativité et la confiance."
            },
        ],
    )


def admissions(request):
    return page(
        request,
        "Admissions",
        "Rejoignez UMM ALQORA d’EXCELLENCE.",
        "Préparez la candidature et la préinscription de votre enfant.",
        [
            {
                "title": "Les cycles proposés",
                "text": "Préscolaire, primaire et collège."
            },
            {
                "title": "Préinscription",
                "text": "Transmettez les premières informations concernant votre enfant."
            },
            {
                "title": "Dossier d'inscription",
                "text": "Consultez les documents nécessaires à l'inscription."
            },
            {
                "title": "Visite de l'établissement",
                "text": "Prenez contact avec l'école pour organiser une visite."
            },
        ],
    )


def actualites(request):
    return page(
        request,
        "Actualités",
        "Les nouvelles de notre école.",
        "Retrouvez les informations et les événements de l'établissement.",
        [
            {
                "title": "Ouverture de l'établissement",
                "text": "Les informations concernant l'ouverture seront communiquées prochainement."
            },
            {
                "title": "Journées portes ouvertes",
                "text": "Les dates seront annoncées prochainement."
            },
        ],
    )


def calendrier(request):
    return page(
        request,
        "Calendrier scolaire",
        "Les dates importantes de l'année.",
        "Retrouvez les événements et les dates importantes de l'établissement.",
        [
            {
                "title": "Rentrée scolaire",
                "text": "Date à confirmer par l'établissement."
            },
            {
                "title": "Vacances scolaires",
                "text": "Les périodes de vacances seront communiquées prochainement."
            },
            {
                "title": "Événements",
                "text": "Les événements seront ajoutés au calendrier."
            },
        ],
    )


def contact(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        messages.success(
            request,
            "Votre message a été validé. Merci de nous avoir contactés."
        )
        return redirect("website:contact")

    return render(request, "website/contact.html", {"form": form})


def connexion(request):
    return render(request, "website/connexion.html")


def preinscription(request):
    form = PreinscriptionForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        messages.success(
            request,
            "Votre formulaire a été validé. L'équipe de l'école pourra vous recontacter."
        )
        return redirect("website:preinscription")

    return render(
        request,
        "website/admissions/preinscription.html",
        {"form": form}
    )


def visite(request):
    form = VisiteForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        messages.success(
            request,
            "Votre demande de visite a été validée."
        )
        return redirect("website:visite")

    return render(request, "website/admissions/visite.html", {"form": form})


def dossier(request):
    return render(request, "website/admissions/dossier.html")


def histoire(request):
    return page(
        request,
        "Notre histoire",
        "Un projet éducatif tourné vers l'avenir.",
        "Découvrez le projet et les ambitions de notre établissement.",
        [
            {
                "title": "Notre établissement",
                "text": "UMM ALQORA d’EXCELLENCE est un projet éducatif situé à Oujda, au Maroc."
            },
            {
                "title": "Notre ambition",
                "text": "Proposer un environnement favorable à l'apprentissage et à l'épanouissement."
            },
        ],
    )


def mission(request):
    return page(
        request,
        "Mission et valeurs",
        "Former et accompagner chaque élève.",
        "Notre projet éducatif repose sur des valeurs essentielles.",
        [
            {
                "title": "Excellence",
                "text": "Encourager chaque élève à progresser."
            },
            {
                "title": "Respect",
                "text": "Favoriser un environnement bienveillant."
            },
            {
                "title": "Autonomie",
                "text": "Développer la responsabilité et l'esprit d'initiative."
            },
        ],
    )


def espaces(request):
    return page(
        request,
        "Nos espaces",
        "Des espaces pour apprendre et découvrir.",
        "Présentation des espaces de l'établissement.",
        [
            {
                "title": "Salles de classe",
                "text": "Des espaces dédiés aux apprentissages."
            },
            {
                "title": "Espaces de découverte",
                "text": "Des lieux adaptés aux activités et aux projets."
            },
        ],
    )


def approche(request):
    return page(
        request,
        "Notre approche pédagogique",
        "Apprendre autrement.",
        "Une pédagogie qui encourage la participation et la curiosité.",
        [
            {
                "title": "Apprentissage actif",
                "text": "L'élève participe activement à ses apprentissages."
            },
            {
                "title": "Accompagnement",
                "text": "Chaque élève bénéficie d'un suivi adapté."
            },
        ],
    )


def cycle(request, nom, titre):
    return page(
        request,
        titre,
        "Un parcours adapté à chaque âge.",
        "Découvrez les objectifs et les apprentissages de ce cycle.",
        [
            {
                "title": "Apprentissages",
                "text": "Des activités adaptées au niveau et au développement des élèves."
            },
            {
                "title": "Accompagnement",
                "text": "Un suivi pédagogique tout au long du parcours scolaire."
            },
        ],
    )


def activites(request):
    return page(
        request,
        "Activités parascolaires",
        "Découvrir et développer ses passions.",
        "Les activités complètent les apprentissages scolaires.",
        [
            {
                "title": "Activités sportives",
                "text": "Développer la coopération et l'esprit d'équipe."
            },
            {
                "title": "Activités artistiques",
                "text": "Encourager l'expression et la créativité."
            },
        ],
    )


def robotique(request):
    return page(
        request,
        "Informatique et robotique",
        "Comprendre, programmer et créer.",
        "Une découverte du numérique et de la logique informatique.",
        [
            {
                "title": "Informatique",
                "text": "Découvrir les outils numériques."
            },
            {
                "title": "Robotique",
                "text": "Développer la logique et la résolution de problèmes."
            },
        ],
    )


def sorties(request):
    return page(
        request,
        "Sorties éducatives",
        "Apprendre en découvrant le monde.",
        "Les sorties permettent de compléter les apprentissages par l'expérience.",
        [
            {
                "title": "Découvertes culturelles",
                "text": "Découvrir le patrimoine et la culture."
            },
            {
                "title": "Découvertes scientifiques",
                "text": "Observer et expérimenter."
            },
        ],
    )