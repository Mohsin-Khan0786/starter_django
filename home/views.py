from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples = [
        {"Name": "Mohsin", "Age": "22"},
        {"Name": "Asad", "Age": "21"},
        {"Name": "Areeb", "Age": "52"},
    ]

    for people in peoples:
        print(people)    

    return render(request, 'home/index.html', context={'peoples': peoples})

 

def success_page(request):
    return HttpResponse("<h2> Hey this is a success page </h2>")



