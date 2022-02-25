from dal import autocomplete
from django import forms

from tags.models import Tag
from .models import Book, Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


AuthorFormSet = forms.modelformset_factory(Author, form=AuthorForm)


class BookForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tags:tag-autocomplete')
    )
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        required=False,
    )

    class Meta:
        model = Book
        fields = '__all__'
