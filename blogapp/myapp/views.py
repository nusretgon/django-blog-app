from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

# http://127.0.0.1:8000
def index(request):
    return HttpResponse("Index")
def details(request):
    return HttpResponse("Details")

def getProductsByCategory(request, category):
    category_text = None
    if category == 'bilgisayar':
        category_text = "bilgisayarlar"
    elif category == 'telefon':
        category_text = 'telefonlar'
    else:
        category_text = 'yanlis secim'
        
    return HttpResponse(category_text)
