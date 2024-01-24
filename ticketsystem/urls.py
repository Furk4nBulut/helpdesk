from django.urls import path, re_path
from ticketsystem.views import showticket, view_dashboard, createTicket, assignedtome, updateticket

urlpatterns = [
    re_path(r'^show/(?P<ticket_id>[0-9]+)', showticket, name='showticket'),
    path('mytickets/', view_dashboard, name='view_dashboard'),
    path('ticketcreate/', createTicket, name='createTicket'),
    path('assigned/', assignedtome, name='assignedtome'),
    re_path(r'^update/(?P<ticket_id>[0-9]+)', updateticket, name='updateticket'),
]
