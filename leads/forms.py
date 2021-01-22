from django.forms import fields
from leads.models import Lead
from django import forms

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            
        )

class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)