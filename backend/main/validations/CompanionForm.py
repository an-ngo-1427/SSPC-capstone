from django.forms import ModelForm
from django import forms
from ..models import Companion
class CompanionForm(ModelForm):

    class Meta:
        model = Companion
        fields = ['breed','weight','age','companion_notes','pet_address','owner']
