
from ..models import User
from django import forms

# define the class of a form
class UserForm(forms.ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model = User

        # Custom fields
        fields =["username", "email",'first_name','last_name']
