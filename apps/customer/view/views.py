from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from ..form import *
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import update_session_auth_hash


@method_decorator(login_required, name='dispatch')
class Customer(TemplateView):
    template_name = 'customer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Customer'
        return context


@method_decorator(login_required, name='dispatch')
class Profile(UpdateView):
    model = User
    template_name = 'profile.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer_app:profile_id')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def changePassword(self):
        pass

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if request.POST['action'] == 'change_password':
            change_form = PasswordChangeForm(request.user, form.data)
            if change_form.is_valid():
                print('valid')
                user = change_form.save()
                update_session_auth_hash(request, user)
        else:
            form_product = BasigCustomerForm(
                request.POST, request.FILES, instance=request.user.customer)
            data = {}
            if form.is_valid() and form_product.is_valid():
                data = form.save()
                form_product.save()
            else:
                data['error'] = form.errors
        return HttpResponseRedirect(reverse_lazy('customer_app:profile_id', kwargs={'pk': request.user.id}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CustomerForm(instance=self.request.user)
        form_customer = BasigCustomerForm(instance=self.request.user.customer)
        password_form = PasswordChangeForm(self.request.user)
        context['title'] = 'Profile'
        context['form_customer'] = form_customer
        context['form'] = form
        context['password_form'] = password_form
        return context
