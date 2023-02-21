from datetime import timedelta

from application.models import Person

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone


class TriangleForm(forms.Form):
    cathetus1 = forms.IntegerField(label='Катет - a', min_value=0)
    cathetus2 = forms.IntegerField(label='Катет - b', min_value=0)


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ("first_name", "last_name", "email")


class EmailForm(forms.Form):
    email = forms.EmailField(max_length=50, required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)
    date = forms.DateTimeField(label="Date sent", initial=timezone.now(), required=True)

    def clean_date(self):
        data = self.cleaned_data['date']
        date2 = timezone.now() + timedelta(days=2)

        if timezone.now() > data or data >= date2:
            raise ValidationError('Error date')

        return data
