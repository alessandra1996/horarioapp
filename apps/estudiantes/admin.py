from django.contrib import admin
from .models import *

# Register your models here.
class Adminregistrado(admin.ModelAdmin):
    list_display =["codigo_alumno","nombre","apellido","telefono","timestamp","actualizado"]
   # form = registradoform
    class Meta:
       model = alumno
class AdminMaterias(admin.ModelAdmin):
    list_display =["codigo_asignaturas","nombre","creditos","numero_horas","codigo_tipo"]
   # form = registradoform
    class Meta:
       model = asignaturas
class AdminTipo(admin.ModelAdmin):
    list_display =["codigo_tipo","nombre"]
   # form = registradoform
    class Meta:
       model = tipo

admin.site.register(alumno,Adminregistrado)        
admin.site.register(asignaturas,AdminMaterias) 
admin.site.register(tipo,AdminTipo) 