
from  django import forms

from main.models import Worker


class Worker_Register(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name', 'surname', 'age', 'experience_year', 'vacancy', 'education', 'skills', 'middle_name']
