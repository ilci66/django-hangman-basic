from multiprocessing import context
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
# from django.views import View # This was used in the docs, both work
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Word, Category
from .forms import WordForm, CategoryForm
import random

categories = [
    {'id': 1, 'name': 'food'},
    {'id': 2, 'name': 'profession'},
    {'id': 3, 'name': 'animal'},
    {'id': 4, 'name': 'family'},
]

words = [
    {'id': 1, 'category': 1, 'text': 'hamburger'},
    {'id': 2, 'category': 1, 'text': 'watermellon'},
    {'id': 3, 'category': 2, 'text': 'teacher'},
    {'id': 4, 'category': 2, 'text': 'engineer'},
    {'id': 5, 'category': 3, 'text': 'lion'},
    {'id': 6, 'category': 3, 'text': 'mouse'},
    {'id': 7, 'category': 4, 'text': 'father'},
    {'id': 8, 'category': 4, 'text': 'son'},
]

class TestView(TemplateView):
    template_name = "test"

    def get(self, request, *args, **kwargs) -> HttpResponse:
        return render(request, 'hang/test.html')


class HomeView(TemplateView):
    template_name = "home"

    def get(self, request, *args, **kwargs):
        context = {'categories': categories}
        return render(request, 'hang/home.html', context)


class WordsView(TemplateView):
    template_name = "words"
    
    words = Word.objects

    def get(self, request, *args, **kwargs):
        form = WordForm()
        context = { 'words_list': words, 'form': form }
        return render(request, 'hang/words.html', context)


class CategoriesView(TemplateView):
    template_name = "categories"
    form_class = CategoryForm
    categories = Category.objects

    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        context = {'form': form, 'categories': categories}
        return render(request, 'hang/categories.html', context)
    
    def post(self, request, *args, **kwargs):
        # form = CategoryForm(request.POST)
        form = self.form_class(request.POST)
        
        # print(form)

        if form.is_valid():

            category = form.save()
            
            print("category ==Z  ",category)

            category.name = category.name.lower()
            category.save()

            print("everything works up to this point")
            return HttpResponseRedirect('/')


class WordView(DetailView):
    template_name = "word-picked"

    def get(self, request, *args, **kwargs):
                
        filtered_categories = list(filter(lambda x: kwargs["id"]== x["category"], words))
        random_word = random.choice(filtered_categories)
        context = {'random_word': random_word}
        return render(request, 'hang/word.html', context)