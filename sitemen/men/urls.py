from django.urls import path, include
from men import views

MainAPP = views.MainAPP()


urlpatterns = [
    path('', MainAPP.index, name = 'main'),
    path('post/<slug:post_slug>/', MainAPP.show_post, name = 'post'),
    path('categories/<slug:cat>/', MainAPP.categories, name = 'categories')
]



