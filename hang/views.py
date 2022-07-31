from django.http import HttpResponse
from django.shortcuts import render
from .models import Word, Category


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
def index(request):

    context = {}
    # return HttpResponse("Eyy, it be workin")

    return render(request, 'hang/home.html', context)