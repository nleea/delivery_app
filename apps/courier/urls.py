from django.urls import path
from .view.views import *

app_name = 'courier_app'

urlpatterns = [
    path('', Courier.as_view(), name='courier')
]
