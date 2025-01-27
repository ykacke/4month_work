from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def profile(request):
    salary = getattr(request.user, 'salary', None)
    return HttpResponse(f'Зарплата: {salary}')