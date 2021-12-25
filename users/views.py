from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    # Check whether setup administrator
    if get_user_model().objects.is_setup_administrator():
        return render(request, 'users/index.html')
    else:
        return redirect(reverse('setup'))


def setup(request):
    # Check whether setup administrator
    if get_user_model().objects.is_setup_administrator():
        return redirect(reverse('index'))

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password != confirm_password:
            pass

        get_user_model().objects.create_superuser(
            username=email,
            email=email,
            password=password,
        )
        return redirect(reverse('index'))

    return render(request, 'users/setup.html')
