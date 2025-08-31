
from django.urls import path
from .views import *
urlpatterns = [
    path('',alltrainee,name='trainee'),
    path('Insert/',insert,name='inserttrainee'),
    path('Update/<int:id>/',update,name='updatetrainee'),
    path('delete/<int:id>/',delete,name='deletetrainee'),
]