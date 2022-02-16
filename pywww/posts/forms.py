from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelectMultiple
from dal import autocomplete

from tags.models import Tag
from .models import Post


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tags:tag-autocomplete')
    )
    class Meta:
        model = Post
        fields = ['title', 'content', 'published', 'sponsored', 'image_file', 'tags']
        labels = {
            'title': 'Tytuł',
            'content': 'Treść',
            'published': 'opublikowany',
            'sponsored': 'sponsorowany',
            'image_file': 'obrazek:'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Dodaj post',
                'title',
                'content',
                'published',
                'sponsored',
                'image_file',
                'tags',
            ),
            ButtonHolder(
                Submit('submit', 'zatwierdź', css_class='btn btn-outline-light me-2'),
                css_class='text-end',
            )
        )
