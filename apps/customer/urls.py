from django.urls import path
from .view.views import *
app_name = 'customer_app'

urlpatterns = [
    path('', Customer.as_view(), name='customer'),
    # path('profile/', Profile.as_view(), name='profile'),
    path('profile/<int:pk>/', Profile.as_view(), name='profile_id')
]
