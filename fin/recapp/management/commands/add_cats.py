from django.core.management.base import BaseCommand, CommandParser
from recapp.models import *

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        names = ['Холодные блюда', 'Горячие блюда', 'Закуски']
        for i in range(len(names)):
            categories = Category(name=names[i])
            categories.save()
        self.stdout.write('Добавлено!')
