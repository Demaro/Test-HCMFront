from django.shortcuts import render, redirect
from .models import Reservacion, Sala
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect

from apps.reserva.forms import ReservaForm


#Visualizacion de reservacion selecionada desde calendario:
def Reserva(request, id_reserva):
    user = request.user
    reserva = Reservacion.objects.filter(id=id_reserva)
    template = "home.html"
    return render(request, template, {'reserva':reserva})


#Funcion para solicitar reservacion
#query de comparacion de sala disponible o reservada
#con requerimientos de reservacion por el empleado.
def Reserva_view(request):
    if request.method == 'POST':
        user = request.user
        form = ReservaForm(request.POST)
        if form.is_valid():
            res = form.save(commit=False)
            res.usuario = request.user
            res.save()
            res.id
            res.capacidad
            res.hora_inicio
            res.hora_termino
            reserva = Reservacion.objects.get(id=res.id)
            try:
                sala = Sala.objects.filter(capacidad=res.capacidad).filter(estado="Disponible" or "Reservada").filter(horario_disp__range=(res.hora_inicio, res.hora_termino)).values_list('id', flat=True)[0]
            except IndexError:
                return render(request, 'notrange.html')

            sala_select = Sala.objects.filter(id=sala)
            return render(request, 'index.html', {'sala_select':sala_select, 'reserva':reserva})
            
    else:
        form = ReservaForm()
    return render(request, 'reserva_form.html', {'form':form})



#BTN para solicitar sala encontrada segun requerimientos:
def Solicita(request, id_sala, id_reserva):
    update = Reservacion.objects.filter(id=id_reserva).update(sala=id_sala)
    estado = Sala.objects.filter(id=id_sala).update(estado="Reservada")
    reserva = Reservacion.objects.filter(id=id_reserva)
    sala    = Sala.objects.filter(id=id_sala)
    return render(request, 'home.html', {'reserva':reserva, 'sala':sala})



#BTN MODIFICAR
def Edit_reserva(request, id_reserva):
    reserva = Reservacion.objects.get(id=id_reserva)
    if request.method == 'GET':
        form = ReservaForm(instance=reserva)
    else: 
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/test/calendario/')
    return render(request, 'reserva_form.html', {'form':form, 'reserva':reserva})

#BTN CONFIRMAR
def Confirma(request, id_reserva, id_sala):
    if request.method == 'GET':
       reserva = Reservacion.objects.get(id=id_reserva)
       sala    = Sala.objects.filter(id=id_sala).update(estado="Confirmada")
       return HttpResponseRedirect('/test/reservacion/%s' % id_reserva)

#BTN ELIMINAR
def DeleteReserva(request, id_reserva, id_sala):
    reserva = Reservacion.objects.get(id=id_reserva)
    sala    = Sala.objects.get(id=id_sala)
    if request.method == 'POST':
        sala.estado = "Disponible"
        reserva.delete()
        sala.save()
        return HttpResponseRedirect('/test/calendario')
    return render(request, 'delete.html', {'reserva':reserva})


#Funcion para calendario por Admin y por Empleado (superuser, active) creador de eventos.
def event(request):
    user = request.user
    if user.is_superuser:
        all_events = Reservacion.objects.all()
        get_event_types = Reservacion.objects.only('sala')

    # if filters applied then get parameter and filter based on condition else return object
        if request.GET:  
            event_arr = []
            if request.GET.get('sala') == "all":
                all_events = Reservacion.objects.filter()
            else:   
                all_events = Reservacion.objects.filter(sala__icontains=request.GET.get('sala'))

            for i in all_events:
                event_sub_arr = {}
                event_sub_arr['title'] = i.event_name
                start_date = date(i.fecha.date(), "%Y-%m-%d")
                start_hora = time(i.hora_inicio.time(), "%Y-%m-%d")
                end_hora = time(i.hora_termino.time(), "%Y-%m-%d")
                end_date = date(i.fecha.date(), "%Y-%m-%d")
                event_sub_arr['start'] = start_date
                event_sub_arr['end'] = end_date
                event_sub_arr['start_hora'] = start_hora
                event_sub_arr['end_hora'] = end_hora
                event_arr.append(event_sub_arr)
            return HttpResponse(json.dumps(event_arr))

        context = {
            "events":all_events,
            "get_event_types":get_event_types,

        }
        return render(request,'calendardemo.html',context)
    elif user.is_active:
        all_events = Reservacion.objects.filter(usuario=request.user).filter(sala__isnull=False)
        get_event_types = Reservacion.objects.only('sala')

    # if filters applied then get parameter and filter based on condition else return object
        if request.GET:  
            event_arr = []
            if request.GET.get('sala') == "all":
                all_events = Reservacion.objects.filter(usuario=request.user).filter(sala__isnull=False)
            else:   
                all_events = Reservacion.objects.filter(sala__icontains=request.GET.get('sala'))

            for i in all_events:
                event_sub_arr = {}
                event_sub_arr['title'] = i.event_name
                start_date = date(i.fecha.date(), "%Y-%m-%d")
                start_hora = time(i.hora_inicio.time(), "%Y-%m-%d")
                end_hora = time(i.hora_termino.time(), "%Y-%m-%d")
                end_date = date(i.fecha.date(), "%Y-%m-%d")
                event_sub_arr['start'] = start_date
                event_sub_arr['end'] = end_date
                event_sub_arr['start_hora'] = start_hora
                event_sub_arr['end_hora'] = end_hora
                event_arr.append(event_sub_arr)
            return HttpResponse(json.dumps(event_arr))

        context = {
            "events":all_events,
            "get_event_types":get_event_types,

        }
        return render(request,'calendardemo.html',context)


