from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from men import views

MainAPP = views.MainAPP()


urlpatterns = [
    path('', MainAPP.index, name = 'main'),
    path('post/<slug:post_slug>/', MainAPP.show_post, name = 'post'),
    path('categories/<slug:cat>/', MainAPP.categories, name = 'categories'),
    path('add-post/', MainAPP.add_post, name = 'add_post'),
    path('about/', MainAPP.about, name = 'about'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



