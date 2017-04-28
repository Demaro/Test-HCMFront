from django.db import models
from django.contrib.auth.models import User


class Sala(models.Model):
    nombre       = models.CharField(max_length=20)
    ubicacion    = models.CharField(max_length=20, blank=True)
    horario_disp = models.CharField(max_length=30)
    estado       = models.CharField(blank=True, max_length=20)
    capacidad    = models.ForeignKey('Cant_personas', on_delete=models.CASCADE, blank=True, null=True)
    insumos      = models.ManyToManyField('Insumo')

    def __str__(self):
        return '{}'.format(self.nombre)

class Insumo(models.Model):
    nombre      = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=40, blank=True)
    stock       = models.IntegerField(blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)


class Reservacion(models.Model):
    sala              = models.ForeignKey('Sala', on_delete=models.CASCADE, blank=True, null=True)
    fecha             = models.DateField(auto_now =False , auto_now_add=False)
    hora_inicio       = models.TimeField(auto_now =False , auto_now_add=False)
    hora_termino      = models.TimeField(auto_now =False , auto_now_add=False)
    capacidad         = models.ForeignKey('Cant_personas')
    insumos           = models.ForeignKey('Cant_insumos')
    usuario           = models.ForeignKey(User)


class Cant_personas(models.Model):
    cantidad    = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.cantidad)


class Cant_insumos(models.Model):
    cantidad    = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.cantidad)




