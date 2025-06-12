from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

class MainAPP():

    def index(self, request):
        return HttpResponse("Hallo")

    def categories(self, request):
        return HttpResponse("Категории")