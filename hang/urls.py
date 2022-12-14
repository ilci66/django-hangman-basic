from django.urls import path, include
from hang.views import CategoriesView, CategoryDeleteView, CategoryEditView, HomeView, TestView, WordDeleteView, WordEditView, WordView, WordsView
from . import views

app_name = 'hang'
urlpatterns = [
    path('category/<int:id>/', WordView.as_view(template_name='word-picked')),
    path('', HomeView.as_view(template_name="home")),
    path('test/', TestView.as_view(template_name='test')),
    path('words/', WordsView.as_view(template_name="words")),
    path('words/<int:id>/edit/', WordEditView.as_view(template_name="word-edit")),
    path('words/<int:id>/delete', WordDeleteView.as_view(template_name="word-delete")),
    path('categories/', CategoriesView.as_view(template_name="categories")),
    path('category/<int:id>/edit', CategoryEditView.as_view(template_name="category-edit")),
    path('category/<int:id>/delete', CategoryDeleteView.as_view(template_name="category-delete"))
]