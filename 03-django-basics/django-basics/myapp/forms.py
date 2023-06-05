from django import forms
from myapp.models import Author, Tag
from myapp.models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(min_length=3, max_length=100)
#     content = forms.CharField(min_length=5, max_length=1000)
#     author = forms.ModelChoiceField(Author.objects.all())
#     tags = forms.ModelMultipleChoiceField(Tag.objects.all())

field_attrs = {'class': 'form-control mb-2'}


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author', 'tag']
        widgets = {
            'title': forms.TextInput(attrs=field_attrs),
            'content': forms.Textarea(attrs=field_attrs),
            'author': forms.Select(attrs=field_attrs),
            'tag': forms.SelectMultiple(attrs=field_attrs),
        }


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    birthDate = forms.DateField(required=False)
    bio = forms.CharField(required=False, widget=forms.Textarea)
