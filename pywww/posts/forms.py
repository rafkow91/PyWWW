from django import forms


class PostForm(forms.Form):
    title = forms.CharField(label='Tytuł')
    content = forms.CharField(widget=forms.Textarea, label='Treść posta')
    sponsored = forms.BooleanField(required=False, label='sponsorowany')
    published = forms.BooleanField(required=False, label='opublikowany')
