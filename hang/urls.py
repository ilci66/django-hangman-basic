from django.urls import path, include
from hang.views import CategoriesView, HomeView, TestView, WordsView
from . import views

urlpatterns = [
    # path('', views.index, name="home"),
    # path('words/', views.words, name="words"),
    # path('categories/', views.categories, name="categories"),
    # path('test/', TestView.as_view(template_name="test"))
    path('', HomeView.as_view(template_name="home")),
    path('test/', TestView.as_view(template_name='test')),
    path('words/', WordsView.as_view(template_name="words")),
    path('categories/', CategoriesView.as_view(template_name="categories"))
]   