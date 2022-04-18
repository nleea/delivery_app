from django.urls import path
from .view.views import *

app_name = 'delivery'

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
