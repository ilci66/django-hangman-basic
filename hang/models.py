from django.db import models

# MOCK DATA -- TO BE ADDED TO THE DATABASE LATER
# categories = [
#     {'id': 1, 'name': 'food'},
#     {'id': 2, 'name': 'profession'},
#     {'id': 3, 'name': 'animal'},
#     {'id': 4, 'name': 'family'},
# ]

# word = [
#     {'id': 1, 'category': 1, 'text': 'hamburger'},
#     {'id': 2, 'category': 1, 'text': 'watermellon'},
#     {'id': 3, 'category': 2, 'text': 'teacher'},
#     {'id': 4, 'category': 2, 'text': 'engineer'},
#     {'id': 5, 'category': 3, 'text': 'lion'},
#     {'id': 6, 'category': 3, 'text': 'mouse'},
#     {'id': 7, 'category': 4, 'text': 'father'},
#     {'id': 8, 'category': 4, 'text': 'son'},
# ]


class Category(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self) -> str:
        return str(self.name)


class Word(models.Model):
    text = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.text)
