from django.db import models

class Recipe(models.Model):
    name = models.TextField(default='', max_length=100, help_text='Название блюда')
    desc = models.CharField(default='', max_length=100, help_text='Описание')
    steps = models.CharField(default='', max_length=100, help_text='Шаги приготовления')
    time = models.DecimalField(max_digits=5, decimal_places=0, help_text='Время приготовления (n часов)')
    pic = models.ImageField(help_text='Изображение')
    tm = models.TextField(default='', max_length=100,help_text='Автор')
class Category(models.Model):
    name = models.CharField(default='', max_length=100, help_text='Название категории')
class RecCat(models.Model):
    category = models.ForeignKey(Category, help_text='Название категории', on_delete=models.CASCADE)
    recs = models.ForeignKey(Recipe, help_text='Рецепты', on_delete=models.CASCADE)