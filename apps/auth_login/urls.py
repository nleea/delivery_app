from django.urls import path
from .view.views import *

app_name = 'auth'

urlpatterns = [
    path('login/', AuthLoginView.as_view(), name='login'),
    path('logout/', AuthLogoutView.as_view(), name='logout'),
    path('signup/', AuthSignupView.as_view(), name='signup')
]
