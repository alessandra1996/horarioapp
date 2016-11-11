from django.contrib import admin
from .models import *

# Register your models here.
class Adminregistrado(admin.ModelAdmin):
    list_display =["codigo_alumno","nombre","apellido","telefono","timestamp","actualizado"]
   # form = registradoform
    class Meta:
       model = Alumno
class AdminMaterias(admin.ModelAdmin):
    list_display =["codigo_asignaturas","nombre","creditos","numero_horas","codigo_tipo"]
   # form = registradoform
    class Meta:
       model = Asignaturas
class AdminTipo(admin.ModelAdmin):
    list_display =["codigo_tipo","nombre"]
   # form = registradoform
    class Meta:
       model = Tipo

admin.site.register(Alumno,Adminregistrado)        
admin.site.register(Asignaturas,AdminMaterias) 
admin.site.register(Tipo,AdminTipo) 