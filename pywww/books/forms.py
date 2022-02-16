from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from dal import autocomplete


from .models import Book, Author
from tags.models import Tag

class BookForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tags:tag-autocomplete')
    )
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='books:tag-autocomplete')
    )
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
        self.helper.layout = Layout(
            Fieldset(
                'Dodawanie książek',
                'title',
                'author',
                'description',
                'available',
                'publication_year',
                'publication_city',
                'language',
                'cover',
                'tags',
            ),
            ButtonHolder(
                Submit('submit', 'zatwierdź', css_class='btn btn-outline-light me-2'),
                css_class='text-end'
            )
        )
