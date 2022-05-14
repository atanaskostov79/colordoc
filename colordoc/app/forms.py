from django import forms
from .models import Document, TxtToDoc

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', )

class TxtToDocForm(forms.ModelForm):
    class Meta:
        model = TxtToDoc
        fields = '__all__'
