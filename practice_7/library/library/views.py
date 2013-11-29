from django.shortcuts import render
from django.template import *
from library.models import *
from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django import forms


class BookListView(ListView):
    template_name = "cbv-books.html"
    model = Book


class BookCardView(DetailView):
    template_name = "cbv-book_data.html"
    queryset = Book.objects.all()


class AuthorsListView(ListView):
    template_name = "cbv-authors.html"
    model = Author


class AuthorCardView(DetailView):
    template_name = "cbv-author_card.html"
    queryset = Author.objects.all()


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/login/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })
