from application.models import Person

from django import forms


class TriangleForm(forms.Form):
    cathetus1 = forms.IntegerField(label='Катет - a', min_value=0)
    cathetus2 = forms.IntegerField(label='Катет - b', min_value=0)


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ("first_name", "last_name", "email")
