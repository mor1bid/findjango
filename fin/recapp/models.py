from django.db import models

class Recipe(models.Model):
    name = models.TextField(default='', max_length=100, help_text='Название блюда')
    desc = models.CharField(default='', max_length=100, help_text='Описание')
    steps = models.CharField(default='', max_length=100, help_text='Шаги приготовления')
    time = models.DecimalField(default=0, max_digits=5, decimal_places=0, help_text='Время приготовления (n часов)')
    pic = models.ImageField(help_text='Изображение')
    tm = models.TextField(default='', max_length=100,help_text='Автор')
class Category(models.Model):
    name = models.CharField(default='', max_length=100, help_text='Название категории')
class RecCat(models.Model):
    category = models.ForeignKey(Category, default='', help_text='Название категории', on_delete=models.SET_DEFAULT)
    recs = models.ForeignKey(Recipe, default='', help_text='Рецепты', on_delete=models.SET_DEFAULT)
class Login(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)