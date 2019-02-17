from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.urls import reverse

# Create your views here.
def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        success_url = reverse('products:list')

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



    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )