from django import forms
from .models import Event
from django_summernote.widgets import SummernoteWidget
from django.contrib.admin.widgets import AdminDateWidget

class DateInput(forms.DateInput):
    input_type = 'date'

class EventForm(forms.ModelForm):
    
    class Meta:
        model = Event
        exclude = ['active', 'slug', 'author']
        widgets = {
            'body': SummernoteWidget(attrs={'width': '100%', 'height': '450px'}),
            'day': DateInput(),
        }