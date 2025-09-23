# your_app_name/forms.py

from django import forms
from .models import Task  # Make sure you're importing the Task model

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['user']

        widgets = {
            'due_date' : forms.DateInput(attrs={'type' : 'date'}),
            'due_time' : forms.TimeInput(attrs={'type' : 'time'}),
        }