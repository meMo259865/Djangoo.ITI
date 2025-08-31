from django.urls import path
from .views import *

urlpatterns = [
    path('',alltracks,name='tracks'),
    path('Insert/',insert,name='inserttrack'),
    path('Delete/<int:id>/',delete,name='deletetrack'),
    path('Update/<int:id>/',update,name='updatetrack'),
]