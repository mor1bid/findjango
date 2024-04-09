from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import random
from .models import *
from .forms import *

def basic(request):
    names = []
    for i in range(6):
        i = random.randint(1, Recipe.objects.count()-1)
        checklist = Recipe.objects.all()
        recipe = Recipe.objects.get(id=checklist[i].pk)
        names.append(recipe.name + ' - ' + recipe.desc + '. Время готовки: ' + str(recipe.time) + ' часов')
    context = {'recs': names}
    return render(request, 'basic.html', context)

def regi(request):
    return render(request, 'regi.html')

def login(request):
    return render(request, 'login.html')

def mkdish(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        recize = Recipe.objects.count()
        if form.is_valid():
            fs = FileSystemStorage()
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
                if myid == rec and myid != 0:
                    fs.save(mypic.name, mypic)
                    recipe.name = myname
                    recipe.desc = mydesc
                    recipe.steps = mysteps
                    recipe.time = mytime
                    recipe.pic = str(request.FILES['pic'])
                    recipe.tm = mytm
                    recipe.save()
                    print('Рецепт дополнен!')
                elif myid > recize:
                    myrecipe = Recipe(name=myname, desc=mydesc, steps=mysteps, time=mytime, tm=mytm)
                    fs.save(mypic.name, mypic)
                    myrecipe.pic = str(request.FILES['pic'])
                    myrecipe.save()
                    print('Рецепт записан! Спасибо!')
                    myid = 0
            form = RecipeForm()
    else:
        form = RecipeForm()
    return render(request, 'mkdish.html', {'form': form })

