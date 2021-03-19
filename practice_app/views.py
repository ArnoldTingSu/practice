from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def index(request):
    return HttpResponse("Hello, welcome to the practice app!")

def new(request):
    return HttpResponse("placeholder for creating a new blog")
def next(request):
    return HttpResponse("welcome to the next page!!")
def create(request):
    return HttpResponse("Create a new blog here!")
def show(request, number):
    if number < 100:
        return HttpResponse(f"placeholder to display {number}, a low number!!!!")
    elif number == 420:
        return HttpResponse(f"placeholder to display {number}, B L A Z E   I T")
    elif number > 100:
        return HttpResponse(f"placeholder to display {number}, a high number!!!!")
def edit(request, number):
    return HttpResponse(f"placeholder to edit page number {number}!!")
def destroy(request, number):
    return HttpResponse(f"the following page number {number} will be destroyed")
def get_post(request):
    if request.method == "GET":
        print("this is a GET request!")
        return redirect('/')
    if request.method == "POST":
        print("this is a POST request!!!")