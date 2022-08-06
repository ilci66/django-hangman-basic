from django.urls import path, include
from hang.views import CategoriesView, HomeView, TestView, WordView, WordsView
from . import views

app_name = 'hang'
urlpatterns = [
    # path('', views.index, name="home"),
    # path('words/', views.words, name="words"),
    # path('categories/', views.categories, name="categories"),
    # path('test/', TestView.as_view(template_name="test"))
    path('<int:id>/', WordView.as_view(template_name='word-picked')),
    path('', HomeView.as_view(template_name="home")),
    path('test/', TestView.as_view(template_name='test')),
    path('words/', WordsView.as_view(template_name="words")),
    path('categories/', CategoriesView.as_view(template_name="categories"), name='categories'),
]