from django.urls import path
from .views import *

urlpatterns = [
    path('Login/',Login),
    path('Logout/',logout),
    path('Register/',register)
]