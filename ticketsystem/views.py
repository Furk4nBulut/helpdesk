# -*- coding: utf-8 -*-

from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ticketsystem.models import *
from .helpdeskforms import CreateTicketForm, UpdateFollowUpForm, UpdateStatusForm

import logging
from django.utils.translation import gettext_lazy as _
from datetime import datetime

logger = logging.getLogger(__name__)

@login_required
def createTicket(request):
    if request.user.is_authenticated:
        alert = _("Fill Form")
        alertcolor = ""
        form = CreateTicketForm()
        initialdata = {'status': '1'}

        if request.POST:
            if request.POST['product'] != '':
                department = Product.objects.get(pk=request.POST['product']).department
                initialdata['department'] = department.pk
                initialdata['createdbyUser'] = request.user.id
                initialdata['product'] = request.POST['product']
                initialdata['priority'] = request.POST['priority']
                initialdata['title'] = request.POST['title']
                initialdata['description'] = request.POST['description']
                initialdata['created_date'] = datetime.now()

                form = CreateTicketForm(initialdata)
                if form.is_valid():
                    try:
                        new_ticket = form.save(commit=True)
                        new_followup = FollowUp(
                            ticket=new_ticket,
                            followup_user=request.user,
                            assigned_user=department.depadmin,
                            followup_date=initialdata['created_date'],
                            followupnote=_('This issue assigned to your department')
                        )
                        new_followup.save()
                        logger.debug("create ticket form has been saved")
                        alert = _("Form Saved")
                        alertcolor = "green"
                    except Exception as e:
                        alert = _("Error Occurred")
                        alertcolor = "red"
                        print(e)
                else:
                    print(_("Form Couldn't Be Saved"))
            else:
                alert = _("Product field couldn't be empty. Please select a product")
                alertcolor = "red"

        return render(request, 'ticketsystem/createticket.html', {'form': form, 'status': alert, 'color': alertcolor})

@login_required
def view_dashboard(request):
    tickets = Ticket.objects.filter(createdbyUser=request.user)
    logger.debug(str(len(tickets)) + " ticket found")
    return render(request, 'ticketsystem/mytickets.html', {'tickets': tickets})

@login_required
def showticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    followups = FollowUp.objects.filter(ticket=ticket_id)
    return render(request, 'ticketsystem/ticketdetails.html', {'ticket': ticket, 'followups': followups})

@login_required
def updateticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    followups = FollowUp.objects.filter(ticket=ticket_id)
    initialdata = {'ticket': ticket_id}
    upstatform = UpdateStatusForm()

    if request.POST:
        initialdata['followupnote'] = request.POST['followupnote']
        initialdata['followup_date'] = datetime.now()
        initialdata['followup_user'] = request.user.id

        if request.POST['assigned_user'] != '':
            initialdata['assigned_user'] = request.POST['assigned_user']
        else:
            initialdata['assigned_user'] = request.user.id

        form = UpdateFollowUpForm(initialdata)

        if form.is_valid():
            form.save(commit=True)
            ticket.status = Status.objects.get(pk=request.POST['status'])
            ticket.save()

    else:
        form = UpdateFollowUpForm()

    return render(request, 'ticketsystem/updateticket.html', {'ticket': ticket, 'followups': followups, 'form': form, 'upstatform': upstatform})

@login_required
def assignedtome(request):
    followups = FollowUp.objects.filter(assigned_user=request.user.pk)
    tickets = [followup.ticket for followup in followups]
    return render(request, 'ticketsystem/assignedtome.html', {'tickets': set(tickets)})
