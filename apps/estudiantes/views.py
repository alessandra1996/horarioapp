from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.edit import FormView
from .forms import *
from .models import *
from apps.estudiantes.models import *
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView


def index(request):
    return render (request,'estudiante/index.html')

def AlumnosView(request):
    if request.method=="POST":
        formulario=alumnoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return redirect('estud_list')
    else:
        formulario=alumnoForm()
    ctx={'form':formulario}
    return render (request,'estudiante/estudiante.html',ctx)

def alumno_List (request):
    alumno=Alumno.objects.all().order_by('codigo_alumno')
    contex={'alumnos':alumno}
    return render(request,'estudiante/alumnoList.html',contex)

def alumno_edit (request):
    alumno=Alumno.object.get(codigo=codigo_alumno)
    if request.method=='POST':
        form=alumnoForm(instance=alumno)
    else:
        form=alumnoForm(request.POST,instance=alumno)    
        if form.is_valid():
            form.save()
        return render(request,'estudiante/estudiante.html', {'form':form})
def alumno_delete(request,codigo_alumno):
    alumno=Alumno.object.get(codigo=codigo_alumno)
    if request.method=='POST':
        alumno.delete()
        return redirect('estud_List')
    return render(request,'estudiante/alumno_delete.html',{'alumno':alumno})

class alumnolist(ListView):
    model=Alumno
    template_name='estudiante/alumno_list.html'
    paginate_by=6


class alumnoCreate (CreateView):
    model = Alumno
    form_class=alumnoForm
    template_name = 'estudiante/estudiante.html'
    success_url= reverse_lazy('estud_list')
    

class alumnoUpdate (UpdateView):
    model = Alumno
    form_class=alumnoForm
    template_name='estudiante/estudiante.html'
    success_url = reverse_lazy ('estud_list')
    

class alumnoDelete (DeleteView):
    model = Alumno
    template_name='estudiante/alumno_delete.html'
    success_url = reverse_lazy ('estud_list')

def AsignaturasView(request):
    if request.method=="POST":
        formulario=asignaturasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return redirect('asig_list')
    else:
        formulario=asignaturasForm()
    ctx={'form':formulario}
    return render (request,'estudiante/asignatura.html',ctx)

def asignatura_List (request):
    asignatura=Asignatura.objects.all().order_by('codigo_asignaturas')
    contex={'asignatura':asignatura}
    return render(request,'estudiante/asignaturaList.html',contex)

def asignatura_edit (request):
    asignatura=Asignatura.object.get(codigo=codigo_asignaturas)
    if request.method=='POST':
        form=asignaturasForm(instance=asignaturas)
    else:
        form=asignaturasForm(request.POST,instance=asignaturas)    
        if form.is_valid():
            form.save()
        return render(request,'estudiante/asignatura.html', {'form':form})

def asignatura_delete(request,codigo_asignaturas):
    asignatura=Asignatura.object.get(codigo=codigo_asignaturas)
    if request.method=='POST':
        asignatura.delete()
        return redirect('asig_List')
    return render(request,'estudiante/asignatura_delete.html',{'asignatura':asignaturas})

class asignaturalist(ListView):
    model=Asignaturas
    template_name='estudiante/asignatura_list.html'
    paginate_by=6


class asignaturaCreate (CreateView):
    model = Asignaturas
    form_class=asignaturasForm
    template_name = 'estudiante/asignatura.html'
    success_url= reverse_lazy('asig_list')
    

class asignaturaUpdate (UpdateView):
    model = Asignaturas
    form_class=asignaturasForm
    template_name='estudiante/asignatura.html'
    success_url = reverse_lazy ('asig_list')
    

class asignaturaDelete (DeleteView):
    model = Asignaturas
    template_name='estudiante/asignatura_delete.html'
    success_url = reverse_lazy ('asig_list')

def DiasView(request):
    if request.method=="POST":
        formulario=diasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return redirect('dias_list')
    else:
        formulario=asignaturasForm()
    ctx={'form':formulario}
    return render (request,'estudiante/dias.html',ctx)

def dias_List (request):
    dias=Dias.objects.all().order_by('codigo_dias')
    contex={'dias':dias}
    return render(request,'estudiante/diasList.html',contex)

def dias_edit (request):
    dias=Sias.object.get(codigo=codigo_dias)
    if request.method=='POST':
        form=diasForm(instance=dias)
    else:
        form=diasForm(request.POST,instance=dias)    
        if form.is_valid():
            form.save()
        return render(request,'estudiante/dias.html', {'form':form})

def dias_delete(request,codigo_dias):
    dias=Dias.object.get(codigo=codigo_dias)
    if request.method=='POST':
        dias.delete()
        return redirect('dias_List')
    return render(request,'estudiante/dias_delete.html',{'dias':dias})

class diaslist(ListView):
    model=Dias
    template_name='estudiante/dias_list.html'
    paginate_by=6


class diasCreate (CreateView):
    model = Dias
    form_class=diasForm
    template_name = 'estudiante/dias.html'
    success_url= reverse_lazy('dias_list')
    

class diasUpdate (UpdateView):
    model = Dias
    form_class=diasForm
    template_name='estudiante/dias.html'
    success_url = reverse_lazy ('dias_list')
    

class diasDelete (DeleteView):
    model = Dias
    template_name='estudiante/dias_delete.html'
    success_url = reverse_lazy ('dias_list')

def PeriodoAcademicoView(request):
    if request.method=="POST":
        formulario=periodo_academicoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return redirect('periodo_list')
    else:
        formulario=periodo_academicoForm()
    ctx={'form':formulario}
    return render (request,'estudiante/periodo.html',ctx)

def periodo_list (request):
    periodo_academico=Periodo_academico.objects.all().order_by('codigo_pa')
    contex={'periodo':periodo_academico}
    return render(request,'estudiante/periodo_list.html',contex)

def periodo_edit (request):
    periodo_academico=Periodo_academico.object.get(codigo=codigo_pa)
    if request.method=='POST':
        form=periodo_academicoForm(instance=periodo_academico)
    else:
        form=periodo_academicoForm(request.POST,instance=periodo_academico)    
        if form.is_valid():
            form.save()
        return render(request,'estudiante/periodo.html', {'form':form})

def periodo_delete(request,codigo_pa):
    periodo_academico=Periodo_academico.object.get(codigo=codigo_pa)
    if request.method=='POST':
        periodo.delete()
        return redirect('periodo_list')
    return render(request,'estudiante/periodo_delete.html',{'periodo':periodo_academico})

class periodoList(ListView):
    model=Periodo_academico
    template_name='estudiante/periodo_list.html'
    paginate_by=4


class periodoCreate (CreateView):
    model = Periodo_academico
    form_class=periodo_academicoForm
    template_name = 'estudiante/periodo.html'
    success_url= reverse_lazy('periodo_list')
    

class periodoUpdate (UpdateView):
    model = Periodo_academico
    form_class=periodo_academicoForm
    template_name='estudiante/periodo.html'
    success_url = reverse_lazy ('periodo_list')
    

class periodoDelete (DeleteView):
    model = Periodo_academico
    template_name='estudiante/periodo_delete.html'
    success_url = reverse_lazy ('periodo_list')
def HoraView(request):
    if request.method=="POST":
        formulario=horaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return redirect('hora_list')
    else:
        formulario=horaForm()
    ctx={'form':formulario}
    return render (request,'estudiante/horas.html',ctx)

def hora_list (request):
    hora=Hora.objects.all().order_by('codigo_hora')
    contex={'hora':hora}
    return render(request,'estudiante/horas_list.html',contex)

def hora_edit (request):
    hora=Hora.object.get(codigo=codigo_hora)
    if request.method=='POST':
        form=horaForm(instance=hora)
    else:
        form=horaForm(request.POST,instance=hora)    
        if form.is_valid():
            form.save()
        return render(request,'estudiante/horas.html', {'form':form})

def hora_delete(request,codigo_hora):
    hora=Hora.object.get(codigo=codigo_hora)
    if request.method=='POST':
        hora.delete()
        return redirect('hora_list')
    return render(request,'estudiante/horas_delete.html',{'hora':hora})

class horaList(ListView):
    model=Hora
    template_name='estudiante/horas_list.html'
    paginate_by=6


class horaCreate (CreateView):
    model = Hora
    form_class=horaForm
    template_name = 'estudiante/horas.html'
    success_url= reverse_lazy('hora_list')
    

class horaUpdate (UpdateView):
    model = Hora
    form_class=horaForm
    template_name='estudiante/horas.html'
    success_url = reverse_lazy ('hora_list')
    

class horaDelete (DeleteView):
    model = Hora
    template_name='estudiante/horas_delete.html'
    success_url = reverse_lazy ('hora_list')

class franja_crearview(FormView):
    template_name='estudiante/franja.html'
    form_class=franjaForm
    success_url=reverse_lazy('franja_list')
    
    def form_valid(self,form):
        form.crear_franja()
        return super(franja_crearview,self).form_valid(form)

class franjaList(ListView):
    template_name='estudiante/franja_list.html'
    model=Franja
    paginate_by=6

def TipoView(request):
    if request.method=="POST":
        formulario=tipoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return redirect('tipo_list')
    else:
        formulario=tipoForm()
    ctx={'form':formulario}
    return render (request,'estudiante/tipo.html',ctx)

def tipo_list (request):
    tipo=Tipo.objects.all().order_by('codigo_tipo')
    contex={'tipo':tipo}
    return render(request,'estudiante/tipo_list.html',contex)

def tipo_edit (request):
    tipo=Tipo.object.get(codigo=codigo_tipo)
    if request.method=='POST':
        form=tipoForm(instance=tipo)
    else:
        form=tipoForm(request.POST,instance=tipo)    
        if form.is_valid():
            form.save()
        return render(request,'estudiante/tipo.html', {'form':form})

def tipo_delete(request,codigo_tipo):
    tipo=Tipo.object.get(codigo=codigo_tipo)
    if request.method=='POST':
        tipo.delete()
        return redirect('tipo_list')
    return render(request,'estudiante/tipo_delete.html',{'tipo':tipo})

class tipoList(ListView):
    model=Tipo
    template_name='estudiante/tipo_list.html'
    paginate_by=3


class tipoCreate (CreateView):
    model = Tipo
    form_class=tipoForm
    template_name = 'estudiante/tipo.html'
    success_url= reverse_lazy('tipo_list')
    

class tipoUpdate (UpdateView):
    model = Tipo
    form_class=tipoForm
    template_name='estudiante/tipo.html'
    success_url = reverse_lazy ('tipo_list')
    

class tipoDelete (DeleteView):
    model = Tipo
    template_name='estudiante/tipo_delete.html'
    success_url = reverse_lazy ('tipo_list')

def JornadaView(request):
    if request.method=="POST":
        formulario=jornadaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return redirect('jornada_list')
    else:
        formulario=jornadaForm()
    ctx={'form':formulario}
    return render (request,'estudiante/jornada.html',ctx)

def jornada_list (request):
    jornada=Jornada.objects.all().order_by('codigo_jornada')
    contex={'jornada':jornada}
    return render(request,'estudiante/jornada_list.html',contex)

def jornada_edit (request):
    jornada=Jornada.object.get(codigo=codigo_jornada)
    if request.method=='POST':
        form=jornadaForm(instance=jornada)
    else:
        form=jornadaForm(request.POST,instance=jornada)    
        if form.is_valid():
            form.save()
        return render(request,'estudiante/jornada.html', {'form':form})

def joranada_delete(request,codigo_jornada):
    jornada=Jornada.object.get(codigo=codigo_jornada)
    if request.method=='POST':
        jornada.delete()
        return redirect('jornada_list')
    return render(request,'estudiante/jornada_delete.html',{'jornada':jornada})

class jornadaList(ListView):
    model=Jornada
    template_name='estudiante/jornada_list.html'
    paginate_by=2


class jornadaCreate (CreateView):
    model = Jornada
    form_class=jornadaForm
    template_name = 'estudiante/jornada.html'
    success_url= reverse_lazy('jornada_list')
    

class jornadaUpdate (UpdateView):
    model = Jornada
    form_class=jornadaForm
    template_name='estudiante/jornada.html'
    success_url = reverse_lazy ('jornada_list')
    

class jornadaDelete (DeleteView):
    model = Jornada
    template_name='estudiante/jornada_delete.html'
    success_url = reverse_lazy ('jornada_list')

def AsignaturaJornadaView(request):
    if request.method=="POST":
        formulario=asig_jornadaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return redirect('asigjornada_list')
    else:
        formulario=asig_jornadaForm()
    ctx={'form':formulario}
    return render (request,'estudiante/asigjornada.html',ctx)

def asigjornada_list (request):
    asig_jornada=Asig_jornada.objects.all().order_by('__all__')
    contex={'jornada':jornada}
    return render(request,'estudiante/asigjornada_list.html',contex)

def asigjornada_edit (request):
    asig_jornada=Asig_jornada.object.get(codigo=__all__)
    if request.method=='POST':
        form=asig_jornadaForm(instance=asig_jornada)
    else:
        form=asig_jornadaForm(request.POST,instance=asig_jornada)    
        if form.is_valid():
            form.save()
        return render(request,'estudiante/asigjornada.html', {'form':form})

def asigjoranada_delete(request,__all__):
    asig_jornada=Asig_jornada.object.get(codigo=__all__)
    if request.method=='POST':
        asig_jornada.delete()
        return redirect('asigjornada_list')
    return render(request,'estudiante/asigjornada_delete.html',{'asigjornada':asig_jornada})

class asigjornadaList(ListView):
    model=Asig_jornada
    template_name='estudiante/asigjornada_list.html'
    paginate_by=6


class asigjornadaCreate (CreateView):
    model = Asig_jornada
    form_class=asig_jornadaForm
    template_name = 'estudiante/asigjornada.html'
    success_url= reverse_lazy('asigjornada_list')
    

class asigjornadaUpdate (UpdateView):
    model = Asig_jornada
    form_class=asig_jornadaForm
    template_name='estudiante/asigjornada.html'
    success_url = reverse_lazy ('asigjornada_list')
    

class asigjornadaDelete (DeleteView):
    model = Asig_jornada
    template_name='estudiante/asigjornada_delete.html'
    success_url = reverse_lazy ('asigjornada_list')

def HorarioJornadaView(request):
    if request.method=="POST":
        formulario=horarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return redirect('horario_list')
    else:
        formulario=horarioForm()
    ctx={'form':formulario}
    return render (request,'estudiante/horario.html',ctx)

def horario_list (request):
    horario=Horario.objects.all().order_by('idhorario')
    contex={'horario':horario}
    return render(request,'estudiante/horario_list.html',contex)

def horario_edit (request):
    horario=Horario.object.get(codigo=idhorario)
    if request.method=='POST':
        form=horarioForm(instance=horario)
    else:
        form=horarioForm(request.POST,instance=horario)    
        if form.is_valid():
            form.save()
        return render(request,'estudiante/horario.html', {'form':form})

def horario_delete(request,idhorario):
    horario=Horario.object.get(codigo=idhorario)
    if request.method=='POST':
        horario.delete()
        return redirect('horario_list')
    return render(request,'estudiante/horario_delete.html',{'horario':horario})

class horarioList(ListView):
    model=Horario
    template_name='estudiante/horario_list.html'
    paginate_by=4


class horarioCreate (CreateView):
    model = Horario
    form_class=horarioForm
    template_name = 'estudiante/horario.html'
    success_url= reverse_lazy('horario_list')
    

class horarioUpdate (UpdateView):
    model = Horario
    form_class=horarioForm
    template_name='estudiante/horario.html'
    success_url = reverse_lazy ('horario_list')
    

class horarioDelete (DeleteView):
    model = Horario
    template_name='estudiante/horario_delete.html'
    success_url = reverse_lazy ('horario_list')