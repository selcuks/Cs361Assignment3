from django import forms
from .models import blogxx

class blogxForm(forms.ModelForm):

    class Meta:
        model = blogxx
        fields = ["name_s", "description_s", "tags_s"]