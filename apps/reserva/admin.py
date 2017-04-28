from django.contrib import admin
from .models import Reservacion, Sala, Cant_personas, Cant_insumos, Insumo



class ReservacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'hora_inicio', 'hora_termino', 'capacidad', 'insumos', 'sala', 'usuario', )
    list_filter  = ('fecha', 'hora_inicio', 'hora_termino', 'capacidad', 'insumos','sala',)
    search_fields = ('sala_nombre', 'capacidad_capacidad', 'insumos__insumo', 'insumos__sala',)
    list_editable = ('fecha','hora_inicio', 'hora_termino', 'capacidad', 'insumos', 'sala',)

class SalaAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'ubicacion', 'horario_disp', 'estado', 'capacidad', 'insumos',)
	list_filter   = ('nombre', 'ubicacion', 'horario_disp', 'estado', 'capacidad', 'insumos', )
	search_fields = ( 'capacidad__cantidad',)
	list_editable = ('nombre', 'ubicacion', 'horario_disp', 'estado', 'capacidad', 'insumos', )

class InsumoAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'descripcion', 'stock',)
	list_filter  = ('nombre',)
	list_editable = ('nombre', 'descripcion', 'stock',)

class Cant_personasAdmin(admin.ModelAdmin):
	list_display = ('id', 'cantidad',)
	list_editable = ('cantidad',)

class Cant_insumosAdmin(admin.ModelAdmin):
	list_display = ('id', 'cantidad',)
	list_editable = ('cantidad',)

# Register your models here.
admin.site.register(Reservacion, ReservacionAdmin)
admin.site.register(Sala, SalaAdmin)
admin.site.register(Insumo, InsumoAdmin)

admin.site.register(Cant_personas, Cant_personasAdmin)
admin.site.register(Cant_insumos, Cant_insumosAdmin)



