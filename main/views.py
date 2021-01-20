from django.shortcuts import render , HttpResponse
from .models import ToDo
from .models import Book


def homepage(request):
    return render (request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list}) 


def books(request):
    book_list = Book.objects.all()
    return render(request, "books.html", {"book_list": book_list}) 


# def go(request):
#     return HttpResponse("This is my first page.") 

def second(request):
    return HttpResponse("test 2 page")

# Create your views here.


def work(request):
    return render(request, "work.html")