from django import forms
from django.http import HttpResponse
from django.conf import settings
from .models import *

class alumnoForm(forms.ModelForm):
	class Meta:
		model= Alumno
		fields=['codigo_alumno','nombre','apellido','direccion','telefono','id_alumno']
	#	labels={'codigo_alumno': 'Codigo','nombre':'Nombre','apellido':'Apellido','direccion':'Direccion','telefono':'Telefono','id_alumno':'Id'}
	#	widgets={'codigo_alumno':forms.TextInput(attrs={'class':'forms.control'}) ,'nombre':forms.TextInput(attrs={'class':'forms.control'}) ,'apellido':forms.TextInput(attrs={'class':'forms.control'}) ,'direccion':forms.TextInput(attrs={'class':'forms.control'}) ,'telefono':forms.TextInput(attrs={'class':'forms.control'}) ,'id_alumno':forms.TextInput(attrs={'class':'forms.control'}) }
	
class periodo_academicoForm(forms.ModelForm):
	class Meta:
		model = Periodo_academico
		fields = ['codigo_pa','nombre']

class diasForm(forms.ModelForm):
	class Meta:
		model = Dias
		fields = ['codigo_dias','dia']

class horaForm(forms.ModelForm):
	class Meta:
		model = Hora
		fields = ['codigo_hora','hora']

class franjaForm(forms.Form):
	codigo_franja=forms.CharField(label=' codigo franja',widget=forms.TextInput(attrs={'class':'forms-control','required':True}))
	codigo_dias_input=forms.ModelChoiceField(Dias.objects.all(),label='codigo dias',widget=forms.Select(attrs={'class':'form-control','required':True}))
	codigo_hora_input=forms.ModelChoiceField(Hora.objects.all(),label='codigo hora',widget=forms.Select(attrs={'class':'form-control','required':True}))

	def crear_franja(self):
		codigo_franja=self.cleaned_data['codigo_franja']
		codigo_dias_input=self.cleaned_data['codigo_dias_input']
		codigo_hora_input=self.cleaned_data['codigo_hora_input']
		franja=Franja(codigo_franja=codigo_franja)
		franja.save()
		franja_d_h = FranjaDiasHora(franja = franja, codigo_dias = codigo_dias_input, codigo_hora = codigo_hora_input)
		franja_d_h.save()

class tipoForm(forms.ModelForm):
	class Meta:
		model = Tipo 
		fields = '__all__'

class asignaturasForm(forms.ModelForm):
	class Meta:
		model = Asignaturas 
		fields = ['codigo_asignaturas','nombre','creditos','numero_horas','codigo_tipo']

class jornadaForm(forms.ModelForm):
	class Meta:
		model = Jornada 
		fields = ['codigo_jornada','nombre']

class asig_jornadaForm(forms.Form):
	codigo_asignaturas=forms.CharField(label='asignatura', widget=forms.TextInput(attrs={'class':'form-control','required':True}))
	codigo_jornada=forms.CharField(label='jornada',widget=forms.TextInput(attrs={'class':'form-control','required':True}))
	Franja.codigo_hora=forms.ModelChoiceField(label='hora',queryset=Franja.objects.all(),widget=forms.Select(attrs={'class':'form-control','required':True}))
	Franja.codigo_dias=forms.ModelChoiceField(label='dias',queryset=Franja.objects.all(),widget=forms.Select(attrs={'class':'form-control','required':True}))
	Franja.codigo_franja=forms.ModelChoiceField(label='franja',queryset=Franja.objects.all(),widget=forms.Select(attrs={'class':'form-control','required=':True}))
		
class horarioForm(forms.Form):
	idhorario=forms.CharField(label='idhorario',widget=forms.TextInput(attrs={'class':'form-control','required':True}))
	codigo_pa=forms.CharField(label='periodo_academico',widget=forms.TextInput(attrs={'class':'form-control','required':True}))
	codigo_alumno=forms.CharField(label='alumno',widget=forms.TextInput(attrs={'class':'form-control','required':True}))
	Asig_jornada.codigo_asignaturas=forms.ModelChoiceField(label='codigo asignaturas',queryset=Asig_jornada.objects.all(),widget=forms.Select(attrs={'class':'form-control','required':True}))
	Asig_jornada.codigo_jornada=forms.ModelChoiceField(label='codigo jornada',queryset=Asig_jornada.objects.all(),widget=forms.Select(attrs={'class':'form-control','required':True}))