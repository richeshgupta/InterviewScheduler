from django import forms
from .models import Interview



class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['start_time','end_time']