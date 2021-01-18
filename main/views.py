from django.shortcuts import render , HttpResponse


def homepage(request):
    return render (request, "index.html")


def test(request):
    return render(request, "test.html")    


# def go(request):
#     return HttpResponse("This is my first page.") 

def second(request):
    return HttpResponse("test 2 page")

# Create your views here.


def work(request):
    return render(request, "work.html")