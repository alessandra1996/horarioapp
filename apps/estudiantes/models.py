from django.db import models


class Alumno(models.Model):
    codigo_alumno = models.CharField(max_length=11)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    telefono = models.CharField(max_length=11)
    direccion = models.CharField(max_length=60)
    id_alumno = models.CharField(max_length=11)
    #email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)#saber el momento en el que se registro
    actualizado = models.DateTimeField(auto_now_add=False,auto_now=True)#saber el momento en el que se hizo un cambio

    def __str__(self):
        return '{}'.format(self.codigo_alumno)

class Periodo_academico(models.Model):
    codigo_pa = models.IntegerField()
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return '{}'.format(self.codigo_pa)

class Dias(models.Model):
    codigo_dias = models.IntegerField()
    dia = models.CharField(max_length=11)

    def __str__(self):
        return self.dia

    def __unicode__(self):
        return self.dia

    class Meta:
        ordering=["codigo_dias"]

class Hora(models.Model):
    codigo_hora = models.IntegerField()
    hora = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.codigo_hora)

class Franja(models.Model):
    codigo_franja = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.codigo_franja)

class FranjaDiasHora(models.Model):
    franja = models.OneToOneField(Franja)
    codigo_dias = models.ForeignKey(Dias)
    codigo_hora = models.ForeignKey(Hora)

class Tipo(models.Model):
    codigo_tipo = models.IntegerField()
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return '{}'.format(self.codigo_tipo)

class Asignaturas(models.Model):
    codigo_asignaturas = models.IntegerField()
    nombre = models.CharField(max_length=60)
    creditos = models.IntegerField()
    numero_horas = models.IntegerField()
    codigo_tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.codigo_asignaturas)

class Jornada(models.Model):
    codigo_jornada = models.IntegerField()
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return '{}'.format(self.codigo_jornada)

class Asig_jornada(models.Model):
    codigo_asignaturas = models.ForeignKey(Asignaturas,on_delete=models.CASCADE)
    codigo_jornada = models.ForeignKey(Jornada,on_delete=models.CASCADE)
    codigo_franja = models.ManyToManyField(Franja)

class Horario(models.Model):
    idhorario = models.IntegerField()
    codigo_pa = models.ForeignKey(Periodo_academico,on_delete=models.CASCADE)
    codigo_alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    codigo_jornada = models.ManyToManyField(Asig_jornada)

    def __str__(self):
        return '{}'.format(self.idhorario)