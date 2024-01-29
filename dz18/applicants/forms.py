from django import forms

from applicants.models import Resume


class CreateResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = "__all__"
        widgets = {
            'date_of_birth': forms.DateTimeInput(attrs={'type': 'date'})
        }