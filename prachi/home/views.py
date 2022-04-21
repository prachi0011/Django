from tkinter import Variable
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    #adding variables
    context = {
        "variable" : "This is variable",
        "var2" : "This is variable 2",
        "myname" : "Prachi"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is template and remove defualt page content.") 
    ##httpresponse use to return string

def education(request):
    return HttpResponse("These are my educations")

def about(request):
    return HttpResponse("This is page is about prachi")

def contact(request):
    return HttpResponse("This is contact page.")