from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published', 'sponsored', 'image_file']
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
        self.helper.add_input(Submit('submit', 'zatwierdź', css_class='btn btn-outline-light me-2'))
