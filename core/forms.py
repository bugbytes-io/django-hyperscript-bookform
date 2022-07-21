from django import forms
from core.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = ('name', 'author')

    def clean_name(self):
        name = self.cleaned_data['name']
        if name.startswith("a"):
            raise forms.ValidationError("Error: We don't want people who's names start with 'a'!")
        return name