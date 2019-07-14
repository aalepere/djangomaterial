from material import *
from django.forms import ModelForm
from app.models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name','last_name']

        layout = Layout('first_name','last_name')
