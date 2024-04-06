from django.db import models

class Recipe(models.Model):
    name = models.TextField(default='', max_length=100, blank='Название блюда')
    desc = models.CharField(default='', max_length=100, blank='Описание')
    steps = models.CharField(default='', max_length=100, blank='Шаги приготовления')
    time = models.DecimalField(max_digits=5, decimal_places=0, blank='Время приготовления (n часов)')
    pic = models.ImageField(blank='Изображение')
    tm = models.TextField(default='', max_length=100, blank='Автор')
class Category(models.Model):
    name = models.CharField(default='', max_length=100, blank='Название категории')
class RecCat(models.Model):
    category = models.ForeignKey(Category, blank='Название категории', on_delete=models.CASCADE)
    recs = models.ForeignKey(Recipe, blank='Рецепты', on_delete=models.CASCADE)