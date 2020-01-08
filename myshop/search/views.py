from os import path

from django.shortcuts import render

# Create your views here.



def search_index(request):
    return render(request,'search/index.html')

