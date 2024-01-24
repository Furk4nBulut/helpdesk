#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from ticketsystem.models import Department, Product, Status, Priority, Ticket, FollowUp
class TicketAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ticket, TicketAdmin)
class FollowUpAdmin(admin.ModelAdmin):
    pass
admin.site.register(FollowUp, FollowUpAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Department, DepartmentAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class StatusAdmin(admin.ModelAdmin):
    pass
admin.site.register(Status, StatusAdmin)

class PriorityAdmin(admin.ModelAdmin):
    pass
admin.site.register(Priority, PriorityAdmin)


