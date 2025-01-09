from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from . import models


def movie_list(request):
    if request.method == 'GET':
        movies_list = models.Movies.objects.all().order_by('-id')
        context = {'movies_list': movies_list}
        return render(request, 'book.html', context=context)


def movie_detail(request, id):
    if request.method == 'GET':
        movie_id = get_object_or_404(models.Movies, id=id)
        context = {'movie_id': movie_id}
        return render(request, 'book_detail.html', context=context)






def about_me(request):
    if request.method == 'GET':
        return HttpResponse("<h1>About Me</h1><p>This is the about me page.</p>")

def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse("<h1>About My Pets</h1><p>This is the About My Pets page.</p>")

def date_time(request):
    current_time = datetime.now()
    return HttpResponse(f"<h1>Current Time</h1><p>Current time is: {current_time}</p>")
