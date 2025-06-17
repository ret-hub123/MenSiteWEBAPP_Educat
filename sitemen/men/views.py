from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from men.models import Men


# Create your views here.



class Categoris:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Категория {self.name}"


class MainAPP:



    def index(self, request):
        all_post = Men.objects.all()
        data = {
            "cats": ["sportmen", "businessmen", "actors", "programmer"],
            "all_posts": all_post
        }
        return render(request, 'men/main page.html', data)


    def show_post(self, request, post_slug):
        post = get_object_or_404(Men, slug = post_slug)
        return render(request, 'men/post.html', {"post": post})


    def categories(self, request, cat):
            if cat not in self.required_categories:
                data = {'men1': Categoris(cat)}
                return Http404()
            else:
                return HttpResponse(f'Categoris: {cat}')


