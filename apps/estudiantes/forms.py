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

class asig_jornadaForm(forms.ModelForm):
	models = asig_jornada
	fields = ['codigo_asignaturas','codigo_jornada','codigo_dias','codigo_hora','codigo_franja']

class horarioForm(forms.ModelForm):
	models = horario
	fields = ['idhorario','codigo_pa','codigo_alumno','codigo_asignaturas','codigo_jornada']


