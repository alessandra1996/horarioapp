from django import forms
from django.http import HttpResponse
from django.conf import settings
from .models import *

class alumnoForm(forms.ModelForm):
	class Meta:
		model= alumno
		fields=['codigo_alumno','nombre','apellido','direccion','telefono','id_alumno']
	#	labels={'codigo_alumno': 'Codigo','nombre':'Nombre','apellido':'Apellido','direccion':'Direccion','telefono':'Telefono','id_alumno':'Id'}
	#	widgets={'codigo_alumno':forms.TextInput(attrs={'class':'forms.control'}) ,'nombre':forms.TextInput(attrs={'class':'forms.control'}) ,'apellido':forms.TextInput(attrs={'class':'forms.control'}) ,'direccion':forms.TextInput(attrs={'class':'forms.control'}) ,'telefono':forms.TextInput(attrs={'class':'forms.control'}) ,'id_alumno':forms.TextInput(attrs={'class':'forms.control'}) }
	
class periodo_academicoForm(forms.ModelForm):
	class Meta:
		model = periodo_academico
		fields = ['codigo_pa','nombre']

class diasForm(forms.ModelForm):
	class Meta:
		model = dias
		fields = ['codigo_dias','dia']

class horaForm(forms.ModelForm):
	class Meta:
		model = hora
		fields = ['codigo_hora','hora']

class franjaForm(forms.ModelForm):
	class Meta:
		model = franja
		fields = '__all__'

class tipoForm(forms.ModelForm):
	class Meta:
		model = tipo 
		fields = '__all__'

class asignaturasForm(forms.ModelForm):
	class Meta:
		model = asignaturas 
		fields = ['codigo_asignaturas','nombre','creditos','numero_horas','codigo_tipo']

class jornadaForm(forms.ModelForm):
	class Meta:
		model = jornada 
		fields = ['codigo_jornada','nombre']

class asig_jornadaForm(forms.Form):
	codigo_asignaturas=forms.CharField(label='asignatura',widget=forms.CharField(attrs={'class':'form-control','reqiered':True})),
	codigo_jornada=forms.CharField(label='jornada',widget=forms.CharField(attrs={'class':'form-control','requiered':True})),
	franja.codigo_hora=forms.ModelChoiceField(label='hora',queryset=franja.objects.all(),widget=forms.Select(attrs={'class':'form-control','requiered':True})),
	franja.codigo_dias=forms.ModelChoiceField(label='dias',queryset=franja.objects.all(),widget=forms.Select(attrs={'class':'form-control','requiered':True})),
	franja.codigo_franja=forms.ModelChoiceField(label='franja',queryset=franja.objects.all(),widget=forms.Select(attrs={'class':'form-control','requiered=':True})),,
				 }
class horarioForm(forms.ModelForm):
	idhorario=forms.CharField(label='idhorario',widget=forms.CharField(attrs={'class':'form-control','reqiered':True})),
	codigo_pa=forms.CharField(label='periodo_academico',widget=forms.CharField(attrs={'class':'form-control','reqiered':True})),
	codigo_alumno=forms.CharField(label='alumno',widget=forms.CharField(attrs={'class':'form-control','reqiered':True})),
	asig_jornada.codigo_asignaturas=forms.ModelChoiceField(label='codigo asignaturas',queryset=asig_jornada.objects.all(),widget=forms.Select(attrs={'class':'form-control','requiered':True})),
	asig_jornada.codigo_jornada=forms.ModelChoiceField(label='codigo jornada',queryset=asig_jornada.objects.all(),widget=forms.Select(attrs={'class':'form-control','requiered':True})),

