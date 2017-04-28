from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from .import views

from reserva.views import Reserva, Reserva_view, Solicita, event, Edit_reserva, Confirma, DeleteReserva

urlpatterns = [

url(r'^reservacion/(?P<id_reserva>\d+)$', (Reserva), name="reser"),
url(r'^reserva/$', (Reserva_view), name="reserva"),
url(r'^solicita/(?P<id_reserva>\d+)/(?P<id_sala>\d+)/$', Solicita, name="solicita"),
url(r'^calendario/$', (event), name="calendario"),
url(r'^calendario/(?P<id_reserva>\d+)$', (Edit_reserva), name="edit"),
url(r'^confirmar/(?P<id_reserva>\d+)/(?P<id_sala>\d+)/$', (Confirma), name="confirma"),
url(r'^eliminar/(?P<id_reserva>\d+)/(?P<id_sala>\d+)/$', (DeleteReserva), name="delete"),


]