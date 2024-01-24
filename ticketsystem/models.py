from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db import models

class Department(models.Model):
    name = models.CharField(_("Department"), max_length=11)
    depadmin = models.ForeignKey(User, related_name='depadmin', verbose_name=_("Department Admin"), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(verbose_name=_("Product"), max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(verbose_name=_("Status"), max_length=15)

    def __str__(self):
        return self.name

class Priority(models.Model):
    name = models.CharField(verbose_name=_("Priority"), max_length=15)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE)
    department = models.ForeignKey(Department, verbose_name=_("Department"), on_delete=models.CASCADE)
    status = models.ForeignKey(Status, verbose_name=_("Status"), on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, verbose_name=_("Priority"), on_delete=models.CASCADE)
    createdbyUser = models.ForeignKey(User, related_name='createdbyuser', verbose_name=_("Creator"), on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_("Title"), max_length=100)
    description = models.CharField(verbose_name=_("Description"), max_length=1000)
    created_date = models.DateTimeField(verbose_name=_("Created Date"), default=datetime.now)

    def __str__(self):
        return self.title

class FollowUp(models.Model):
    followupnote = models.CharField(verbose_name=_("Comment"), max_length=1000)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    followup_date = models.DateTimeField(verbose_name=_("Modified Date"), blank=True, null=True)
    followup_user = models.ForeignKey(User, related_name='followup_user', verbose_name=_("Comment by"), on_delete=models.CASCADE)
    assigned_user = models.ForeignKey(User, related_name='assigned_user', verbose_name=_("Assign to"), on_delete=models.CASCADE)

    def __str__(self):
        return f"FollowUp for Ticket: {self.ticket.title}"
