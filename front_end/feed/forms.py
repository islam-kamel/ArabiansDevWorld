from django import forms

from .models import Post


class PostCreateForm(forms.Form):
    title = forms.CharField(label="عنوان التدوينة")
    content = forms.CharField(label="محتوي التدوينة", widget=forms.Textarea)


class PostUpdateForm(forms.ModelForm):
    title = forms.CharField(label="عنوان التدوينة")
    content = forms.CharField(label="محتوي التدوينة", widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ["title", "content"]
