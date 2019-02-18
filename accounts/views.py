from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.urls import reverse

# Create your views here.
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

def register_view(request):
    form = RegisterForm()
    success_url = reverse('products:list')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

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