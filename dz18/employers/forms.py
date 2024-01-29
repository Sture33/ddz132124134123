from django import forms

from employers.models import Vacancy


class CreateVacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = "__all__"
