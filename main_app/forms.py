from django.forms import ModelForm
from .models import Maintainance

class MaintainForm(ModelForm):
    class Meta:
        model = Maintainance
        fields = ['date', 'maintain']