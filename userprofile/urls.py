from django.urls import path
from userprofile.views import loginview, logout

urlpatterns = [
    path('login/', loginview, name='loginview'),
    path('logout/', logout, name='logout'),
]
