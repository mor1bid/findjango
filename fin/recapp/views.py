from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import random
from .models import *

def basic(request):
    names = []
    for i in range(6):
        i = random.randint(1, Recipe.objects.count())
        recipe = Recipe.objects.get(pk=i)
        names.append(recipe.name + ' - ' + recipe.desc + '. Время готовки: ' + str(recipe.time) + ' часов')
    context = {'recs': names}
    return render(request, 'basic.html', context)

def regi(request):
    return render(request, 'regi.html')

