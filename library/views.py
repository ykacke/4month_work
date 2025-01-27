from datetime import datetime
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models
from django.views.generic import ListView, DetailView, TemplateView
from .models import Books


class SearchView(ListView):
    template_name = 'library/search.html'
    context_object_name = 'movie_list'


    def get_queryset(self):
        return Books.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class MovieListView(ListView):
    model = models.Movie
    context_object_name = 'movie_list'
    template_name = 'movie_list.html'

class MovieDetailView(DetailView):
    model = models.Movie
    context_object_name = 'movie_detail'
    template_name = 'movie_detail.html'


class SearchForm:
    pass


class BookSearchView(ListView):
    model = Books
    template_name = 'book.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = Books.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        context['q'] = self.request.GET.get('q')
        return context





class AboutMeView(TemplateView):
    template_name = 'about_me.html'

class AboutMyPetsView(TemplateView):
    template_name = 'about_my_pets.html'

class DateTimeView(TemplateView):
    template_name = 'current_time.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_time = datetime.now()
        context['current_time'] = current_time
        return context
