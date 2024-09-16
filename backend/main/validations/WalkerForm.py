from django import forms
from ..models import Walker
class WalkerForm(forms.ModelForm):
    class Meta:
        model = Walker
        fields = ['user','bio','rating','certified']
