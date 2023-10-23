from django import forms

class FillingForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    dob = forms.DateField(required=True)
    age = forms.IntegerField(required=True)
    # Add other form fields here
