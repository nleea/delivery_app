from django.urls import path
from .view.views import *
app_name = 'customer_app'

urlpatterns = [
    path('', Customer.as_view(), name='customer')
]
