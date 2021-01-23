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
    title = form["book_title"]
    subtitle = form["book_subtitle"]
    description = form["book_description"]
    price = form["book_price"]
    genre = form["book_genre"]
    author = form["book_author"]
    year = form["book_year"]
    book = Book(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    book.save()
    return redirect(books)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def marked_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test) 

def nomarked_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)
    
def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect(books)   

def marked_book(request, id):
    book = Book.objects.get(id=id)
    book.is_favorite = True 
    book.save()
    return redirect(books)  

def nomarked_book(request, id):
    book = Book.objects.get(id=id)
    book.is_favorite = False 
    book.save()
    return redirect(books)  

# def book_1(request):
#     book_list = Book.objects.all()
#     return render(request, "books_detail.html", {"book_list": book_list})     

# def info_book(request, id):
#     book = Book.objects.get(id=id)
#     book.save()
#     return redirect(book_1)  

def info_book(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'books_detail.html', {'book': book})

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)    

def close_book(request, id):
    book = Book.objects.get(id=id)
    book.is_closed = not book.is_closed
    book.save()
    return redirect(books)


