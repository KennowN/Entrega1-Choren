from django import forms

class CrearCarniceriaForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    calle = forms.CharField(max_length=50, required=True)
    altura = forms.IntegerField(required=True)
    localidad = forms.CharField(max_length=50, required=True)
    telefono = forms.IntegerField(required=True)

class CrearVerduleriaForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    calle = forms.CharField(max_length=50, required=True)
    altura = forms.IntegerField(required=True)
    localidad = forms.CharField(max_length=50, required=True)
    telefono = forms.IntegerField(required=True)

class CrearPanaderiaForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    calle = forms.CharField(max_length=50, required=True)
    altura = forms.IntegerField(required=True)
    localidad = forms.CharField(max_length=50, required=True)
    telefono = forms.IntegerField(required=True)