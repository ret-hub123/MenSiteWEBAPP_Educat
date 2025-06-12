from django.urls import path, include
from men import views

MainAPP = views.MainAPP()


urlpatterns = [
    path('', MainAPP.index),
    path('categories/', MainAPP.categories)
]


