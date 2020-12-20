from django import forms
from .models import one


class oneForm(forms.ModelForm):
    class Meta:
        model = one
        fields = ["question", "answer","comment"]