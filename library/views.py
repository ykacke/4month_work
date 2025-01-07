from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def about_me(request):
    if request.method == "GET":
        return HttpResponse('Мое имя Адина')

def about_my_pets(request):
    if request.method == "GET":
        return HttpResponse('у меня нету питомца, но хотелось бы')

def data_time(request):
    if request.method == "GET":
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return HttpResponse(f'настоящее время и дата {current_time}')