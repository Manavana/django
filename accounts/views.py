from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy

from .models import accountUser


class AccountLogoutView(LogoutView):
    template_name = 'accounts/logout.html'


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'


def login_view(request):
    form = LoginForm()
    success_url = reverse('products:list')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(
                username=username,
                password=password
            )

            if user and user.is_active:
                login(request, user)

                return redirect(success_url)

    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )


class AccountRegistrationView(CreateView):
    model = accountUser
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('products:list')

    def post(self, *args, **kwargs):
        response = super(RegistrationView, self).post(*args, **kwargs)
        login(self.request, self.object)
        return response


def register_view(request):
    form = RegisterForm()
    success_url = reverse('products:list')

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()

            if user and user.is_active:
                login(request, user)

                return redirect(success_url)

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )