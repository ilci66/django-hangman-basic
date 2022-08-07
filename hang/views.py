from multiprocessing import context
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
# from django.views import View # This was used in the docs, both work
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Word, Category
from .forms import WordForm, CategoryForm
import random

# categories = [
#     {'id': 1, 'name': 'foodd'},
#     {'id': 2, 'name': 'profession'},
#     {'id': 3, 'name': 'animal'},
#     {'id': 4, 'name': 'family'},
# ]

# words = [
#     {'id': 1, 'category': 1, 'text': 'hamburger'},
#     {'id': 2, 'category': 1, 'text': 'watermellon'},
#     {'id': 3, 'category': 2, 'text': 'teacher'},
#     {'id': 4, 'category': 2, 'text': 'engineer'},
#     {'id': 5, 'category': 3, 'text': 'lion'},
#     {'id': 6, 'category': 3, 'text': 'mouse'},
#     {'id': 7, 'category': 4, 'text': 'father'},
#     {'id': 8, 'category': 4, 'text': 'son'},
# ]

class TestView(TemplateView):
    template_name = "test"

    def get(self, request, *args, **kwargs) -> HttpResponse:
        return render(request, 'hang/test.html')


class HomeView(TemplateView):
    template_name = "home"

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        print("categories 00>>", categories)
        context = {'categories': categories}
        return render(request, 'hang/home.html', context)


class WordsView(TemplateView):
    template_name = "words"
    form_class = WordForm

    def get(self, request, *args, **kwargs):
        words = Word.objects.all()
        form = WordForm()
        context = { 'words_list': words, 'form': form }
        return render(request, 'hang/words.html', context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            word = form.save()

            word.text = word.text.lower()
            word.save()

            return HttpResponseRedirect('/words')


class CategoriesView(TemplateView):
    template_name = "categories"
    form_class = CategoryForm

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        form = CategoryForm()
        context = {'form': form, 'categories': categories}
        return render(request, 'hang/categories.html', context)
    
    def post(self, request, *args, **kwargs):
        # form = CategoryForm(request.POST)
        form = self.form_class(request.POST)
        
        # print(form)

        if form.is_valid():

            category = form.save()

            category.name = category.name.lower()
            category.save()

            print("everything works up to this point")
            return HttpResponseRedirect('/')


class WordDeleteView(DetailView):
    template_name = "word-delete"
    form_class = WordForm

    def get(self, request, *args, **kwargs):
        word = Word.objects.get(id=kwargs["id"])
        context = {'word': word}

        return render(request, 'hang/word-delete.html', context)

    def post(self, request, *args, **kwargs):
        print("wanna delete this => ", kwargs["id"])
        form = self.form_class(request.POST)
        if form.is_valid:
            word = Word.objects.get(id=kwargs["id"])
            word.delete()
            return HttpResponseRedirect('/words/')


class CategoryDeleteView(DetailView):
    template_name = "category-delete"
    form_class = CategoryForm

    def get(self, request, *args, **kwargs):
        category = Category.objects.get(id=kwargs["id"])
        context = {'category': category}
        return render(request, 'hang/category-delete.html', context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid:
            category = Category.objects.get(id=kwargs["id"])
            category.delete()
            return HttpResponseRedirect('/categories')


class CategoryEditView(DetailView):
    template_name = "category-edit"
    form_class = CategoryForm

    def get(self, request, *args, **kwargs):
        category = Category.objects.get(id=kwargs["id"])
        form = self.form_class(instance=category)

        print("form ==> ", form )
        
        context = {'form': form}
        return render(request, 'hang/category-edit.html', context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid:
            category = form.save()

            category.name = category.name.lower()
            category.save()

            return HttpResponseRedirect('/')            


class WordView(DetailView):
    template_name = "word-picked"
    
    def get(self, request, *args, **kwargs):
        words = Word.objects.all()
        filtered_categories = list(filter(lambda x: kwargs["id"]== x["category"], words))
        random_word = random.choice(filtered_categories)
        context = {'random_word': random_word}
        return render(request, 'hang/word.html', context)