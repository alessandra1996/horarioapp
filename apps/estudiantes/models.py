from django.db import models


class alumno(models.Model):
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

class periodo_academico(models.Model):
    codigo_pa = models.IntegerField()
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return '{}'.format(self.codigo_pa)

class dias(models.Model):
    codigo_dias = models.IntegerField()
    dia = models.CharField(max_length=11)

    def __str__(self):
        return '{}'.format(self.codigo_dias)
    class Meta:
        ordering=["codigo_dias"]

class hora(models.Model):
    codigo_hora = models.IntegerField()
    hora = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.codigo_hora)

class franja(models.Model):
    codigo_franja = models.IntegerField()
    codigo_dias = models.ManyToManyField(dias)
    codigo_hora = models.ManyToManyField(hora)

    def __str__(self):
        return '{}'.format(self.codigo_franja)

class tipo(models.Model):
    codigo_tipo = models.IntegerField()
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return '{}'.format(self.codigo_tipo)

class asignaturas(models.Model):
    codigo_asignaturas = models.IntegerField()
    nombre = models.CharField(max_length=60)
    creditos = models.IntegerField()
    numero_horas = models.IntegerField()
    codigo_tipo = models.ForeignKey(tipo,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.codigo_asignaturas)

class jornada(models.Model):
    codigo_jornada = models.IntegerField()
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return '{}'.format(self.codigo_jornada)

class asig_jornada(models.Model):
    codigo_asignaturas = models.ForeignKey(asignaturas,on_delete=models.CASCADE)
    codigo_jornada = models.ForeignKey(jornada,on_delete=models.CASCADE)
    franja.codigo_hora = models.ManyToManyField(franja)
    franja.codigo_dias = models.ManyToManyField(franja)
    franja.codigo_franja = models.ManyToManyField(franja)

class horario(models.Model):
    idhorario = models.IntegerField()
    codigo_pa = models.ForeignKey(periodo_academico,on_delete=models.CASCADE)
    codigo_alumno = models.ForeignKey(alumno,on_delete=models.CASCADE)
    asig_jornada.codigo_asignaturas = models.ManyToManyField(asig_jornada)
    asig_jornada.codigo_jornada = models.ManyToManyField(asig_jornada)

    def __str__(self):
        return '{}'.format(self.idhorario)
