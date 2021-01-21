from django.shortcuts import render , HttpResponse, redirect
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


def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)  

def add_book(request):
    form = request.POST
    text = form["book_text"] 
    book = Book(text=test)
    book.save()
    return redirect(books)   