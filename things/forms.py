"""Forms of the project."""
import django.forms as forms
from .models import Thing

# Create your forms here.
class Form(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'description': forms.Textarea(),
            'quantity': forms.NumberInput(),
        }
