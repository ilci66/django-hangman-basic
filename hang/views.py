from django.views.generic import TemplateView
# from django.views import View # This was used in the docs, both work
from django.http import HttpResponse
from django.shortcuts import render
from .models import Word, Category
from .forms import WordForm, CategoryForm


categories = [
    {'id': 1, 'name': 'food'},
    {'id': 2, 'name': 'profession'},
    {'id': 3, 'name': 'animal'},
    {'id': 4, 'name': 'family'},
]

word = [
    {'id': 1, 'category': 1, 'text': 'hamburger'},
    {'id': 2, 'category': 1, 'text': 'watermellon'},
    {'id': 3, 'category': 2, 'text': 'teacher'},
    {'id': 4, 'category': 2, 'text': 'engineer'},
    {'id': 5, 'category': 3, 'text': 'lion'},
    {'id': 6, 'category': 3, 'text': 'mouse'},
    {'id': 7, 'category': 4, 'text': 'father'},
    {'id': 8, 'category': 4, 'text': 'son'},
]

# Create your views here.
# def index(request):

#     context = {}
#     # return HttpResponse("Eyy, it be workin")

#     return render(request, 'hang/home.html', context)

# def words(request):

#     context = {}

#     return render(request, 'hang/words.html', context)


# def categories(request):

#     context = {}

#     return render(request, 'hang/categories.html', context)


class TestView(TemplateView):
    template_name = "test"

    # def get(self) -> HttpResponse:
    #     return HttpResponse("tecrübe")


    def get(self, request, *args, **kwargs) -> HttpResponse:
        return render(request, 'hang/test.html')


class HomeView(TemplateView):
    template_name = "home"
    context = {}
    def get(self, request, *args, **kwargs):
        return render(request, 'hang/home.html', {"name": "name"})


class WordsView(TemplateView):
    template_name = "words"
    # content = {}

    def get(self, request, *args, **kwargs):
        return render(request, 'hang/words.html')

class CategoriesView(TemplateView):
    template_name = "categories"
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, 'hang/categories.html')