from django import forms
from .models import Apply_Institution

class ApplyInstitutionForm(forms.ModelForm):
    class Meta:
        model = Apply_Institution
        fields = ['name','address ','city ','state','country','postal_code', 'email','phone', 'date_of_est','type','principal',  'no_students', 'no_teachers',]