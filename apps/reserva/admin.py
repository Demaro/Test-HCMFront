from django.contrib import admin
from apps.reserva.models import Reservacion, Sala



class ReservacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'hora_inicio', 'hora_termino', 'capacidad', 'insumos', 'sala', 'usuario', )
    list_filter  = ('fecha', 'hora_inicio', 'hora_termino', 'capacidad', 'insumos','sala',)
    search_fields = ('sala_nombre', 'capacidad_capacidad', 'insumos__insumo', 'insumos__sala',)
    list_editable = ('fecha','hora_inicio', 'hora_termino', 'capacidad', 'insumos', 'sala',)

class SalaAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'ubicacion', 'horario_disp', 'estado', 'capacidad',)
	list_filter   = ('nombre', 'ubicacion', 'horario_disp', 'estado', 'capacidad', )
	search_fields = ( 'capacidad__cantidad',)
	list_editable = ('nombre', 'ubicacion', 'horario_disp', 'estado', 'capacidad',)

# Register your models here.
admin.site.register(Reservacion, ReservacionAdmin)

admin.site.register(Sala, SalaAdmin)

