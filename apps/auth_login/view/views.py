from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login
# from django.contrib.auth.models import User
from ..form import *
# Create your views here.


class AuthLoginView(LoginView):
    next_page = reverse_lazy('delivery:home')
    template_name = 'login.html'
    title = 'Login'
    form_class = FormsAuthentication

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.next_page)
        return super().dispatch(request, *args, **kwargs)

    def get_redirect_url(self) -> str:
        return super().get_redirect_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('auth:login')
    template_name = 'login.html'


class AuthSignupView(FormView):
    template_name = 'signup.html'
    form_class = AuthForms
    success_url = reverse_lazy('delivery:home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('delivery:home'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Signup'
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form['email'].data
            user.save()
            # login(request, user,
            #       backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect(self.success_url, *args, **kwargs)
        else:
            context = self.get_context_data(**kwargs)
            context['error'] = form.errors.values()
            return render(request, self.template_name, context)
