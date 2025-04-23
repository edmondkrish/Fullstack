from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['name','author','description','published_date','url']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'published_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'url':forms.URLInput(attrs={'class':'form-control'})    
        }