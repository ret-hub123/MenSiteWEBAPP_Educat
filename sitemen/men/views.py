from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import title

from men.models import Men, Category
from men.forms import AddPostMen


# Create your views here.

class MainAPP:
    required_categories = ["sportmen", "bussnesmen", "actors", "programmer"]

    def index(self, request):
        all_post = Men.objects.all()
        data = {
            "posts": all_post,
            "title": "Актуальные посты"
        }
        return render(request, 'men/main_page.html', data)


    def show_post(self, request, post_slug):
        post = get_object_or_404(Men, slug = post_slug)
        return render(request, 'men/post.html', {"post": post})


    def categories(self, request, cat):
            if cat not in self.required_categories:
                raise Http404("Выбранная категория не недоступна")
            else:
                posts = Men.objects.filter(cat__slug=cat)
                data = {
                    "posts": posts,
                    "title": f"Посты категории {get_object_or_404(Category, slug = cat).name}"
                }

                return render(request, 'men/main_page.html', data)


    def add_post(self, request):
        if request.POST:
            form = AddPostMen(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = AddPostMen()

        data = {
            'title': "Форма добавления поста",
            'form': form
        }
        return render(request, 'men/add_post.html', data)

    def about(self, request):
        data = {
            'title': "О проекте",
        }
        return render(request, 'men/about.html', data)