from django.urls import include, path, re_path
from helpdesk.views import index
from django.contrib import admin

urlpatterns = [
    path('', index, name='index'),
    path('accounts/', include('userprofile.urls')),
    path('admin/', admin.site.urls),
    path('ticketsystem/', include('ticketsystem.urls')),
]
