from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'available', 'publication_year', 'publication_city', 'language',
                  'cover', 'tags']
        labels = {
            'title': 'Tytuł:',
            'author': 'Autorzy: (wybierz zaznaczając odpowiednie nazwiska)',
            'description': 'Opis:',
            'available': 'dostępna',
            'language': 'Język:',
            'publication_year': 'Rok wydania:',
            'publication_city': 'Miejsce wydania:',
            'cover': 'Okładka:',
            'tags': 'Tagi:'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'zatwierdź', css_class='btn btn-outline-light me-2'))
