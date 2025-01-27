from django.http import HttpResponse
from django.shortcuts import render
from . import models, forms
from django.views import generic

class BookListView(generic.ListView):
    model = models.BookParser
    template_name = 'parser/book_list.html'
    context_object_name = 'book_list'


    def get_(self):
        return self.model.objects.all()



class BookDetailView(generic.DetailView):
    template_name = 'parser/book_detail.html'
    context_object_name = 'book_detail'
    forms_class = forms.BookParser

    def post(self, request, *args, **kwargs):
        form = self.forms_class(request.POST)
        if form.is_valid():
            form.parser_data
            return HttpResponse('Парсинг завершен.')
        else:
            return super(BookListView, self).post(request, *args, **kwargs)
