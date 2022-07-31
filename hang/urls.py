from django.urls import path, include
from hang.views import TestView
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('words/', views.words, name="words"),
    path('categories/', views.categories, name="categories"),
    # path('test/', TestView.as_view(template_name="test"))
    path('test/', TestView.as_view(template_name='test'))

]