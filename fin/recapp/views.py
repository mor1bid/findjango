from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import random
from .models import *
from .forms import *

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

def mkdish(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        recize = Recipe.objects.count()
        if form.is_valid():
            myid = form.cleaned_data['rec']
            myname = form.cleaned_data['name']
            mydesc = form.cleaned_data['desc']
            mysteps = form.cleaned_data['steps']
            mytime = form.cleaned_data['time']
            mypic = form.cleaned_data['pic']
            mytm = form.cleaned_data['tm']
            for i in range(1, recize):
                recipe = Recipe.objects.get(pk=i)
                rec = recipe.pk
                if myid == rec:
                    fs = FileSystemStorage()
                    fs.save(mypic.name, mypic)
                    rec.name = myname
                    rec.desc = mydesc
                    rec.steps = mysteps
                    rec.time = mytime
                    rec.pic = str(request.FILES['pic'])
                    rec.tm = mytm
                    rec.save()
                    print('Рецепт дополнен!')
                elif i == recize or myid > recize:
                    recipes = Recipe(name=myname, desc=mydesc, steps=mysteps, time=mytime, tm=mytm)
                    print('Рецепт записан! Спасибо!')
    else:
        form = RecipeForm()
    return render(request, 'addwim.html', {'form': form })

