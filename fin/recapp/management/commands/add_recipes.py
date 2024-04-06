from django.core.management.base import BaseCommand, CommandParser
from recapp.models import *

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        names = ['Чудо-мясо', 'Фрикасе из огненного муравья', 'Омлет', 'Стейк из брамина', 'Хрустящий мутафрукт', 'Чипсы']
        descs = ['Эти консервы содержат от 91 до 93% жареных мозгов и от 7 до 9% костного топленого жира; они очень вкусны', 'Если сырое мясо посолить, то через некоторое время оно начнет выделять сок', 'Вкусное, легкое, питательное блюдо, в состав которого входят овощи', 'Одно из самых деликатесных блюд мясной кулинарии', 'Пища лучше усваивается, если ее едят с аппетитом', 'Вкусное и весьма питательное блюдо – печень в конверте']
        times = [1, 2, 3, 0, 5, 6]
        for i in range(len(names)):
            recipes = Recipe(name=names[i], desc=descs[i], time=times[i])
            recipes.save()
        self.stdout.write('Добавлено!')
