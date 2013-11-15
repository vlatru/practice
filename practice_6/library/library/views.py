from django.shortcuts import render
from django.template import Template
from django.template import Context
from library.models import Author
from library.models import Book
import datetime


def home(request):
    context = {'ts': datetime.datetime.now()}
    return render(request, 'home.html', context)


def books(request):
    context = {'books': Book.objects.all()}
    return render(request, 'books.html', context)


def book(request, book_id):
    context = {'book': Book.objects.get(id=book_id)}
    return render(request, 'book.html', context)


def author(request, author_id):
    context = {'author': Author.objects.get(id=author_id)}
    return render(request, 'author.html', context)


def authors(request):
    context = {'authors': Author.objects.all()}
    return render(request, 'authors.html', context)
