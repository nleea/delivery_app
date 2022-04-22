from django.views.generic import TemplateView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from ..form import *


@method_decorator(login_required, name='dispatch')
class Customer(TemplateView):
    template_name = 'customer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Customer'
        return context


@method_decorator(login_required, name='dispatch')
class Profile(FormView):
    model = User
    template_name = 'profile.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer_app:profile')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = CustomerForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url, *args, **kwargs)
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Profile'
        return context
