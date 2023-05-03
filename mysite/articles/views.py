from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def article(request):
    return render(request, "article.html")


def article2(request):
    return render(request, "article2.html")


def article3(request):
    return render(request, "article3.html")
