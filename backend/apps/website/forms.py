from django import forms


class ContactForm(forms.Form):
    nom = forms.CharField(
        label="Nom complet",
        max_length=150,
        widget=forms.TextInput(attrs={"placeholder": "Votre nom"})
    )

    email = forms.EmailField(
        label="Adresse e-mail",
        widget=forms.EmailInput(attrs={"placeholder": "votre@email.com"})
    )

    telephone = forms.CharField(
        label="Téléphone",
        max_length=30,
        widget=forms.TextInput(attrs={"placeholder": "+212 ..."})
    )

    sujet = forms.CharField(
        label="Sujet",
        max_length=150
    )

    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={"rows": 5})
    )


class PreinscriptionForm(forms.Form):
    nom_parent = forms.CharField(label="Nom du parent", max_length=150)
    email = forms.EmailField(label="Adresse e-mail")
    telephone = forms.CharField(label="Téléphone", max_length=30)

    nom_enfant = forms.CharField(label="Nom de l'enfant", max_length=150)

    date_naissance = forms.DateField(
        label="Date de naissance",
        widget=forms.DateInput(attrs={"type": "date"})
    )

    cycle = forms.ChoiceField(
        label="Cycle souhaité",
        choices=[
            ("prescolaire", "Préscolaire"),
            ("primaire", "Primaire"),
            ("college", "Collège"),
        ]
    )


class VisiteForm(forms.Form):
    nom = forms.CharField(label="Nom complet", max_length=150)
    email = forms.EmailField(label="Adresse e-mail")
    telephone = forms.CharField(label="Téléphone", max_length=30)

    date_visite = forms.DateField(
        label="Date souhaitée",
        widget=forms.DateInput(attrs={"type": "date"})
    )

    message = forms.CharField(
        label="Message",
        required=False,
        widget=forms.Textarea(attrs={"rows": 4})
    )