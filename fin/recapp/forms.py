from django import forms

class RecipeForm(forms.Form):
    rec = forms.DecimalField(label='Номер рецепта')
    name = forms.TextInput(default='', max_length=100, help_text='Название блюда')
    desc = forms.CharField(default='', max_length=100, help_text='Описание')
    steps = forms.CharField(default='', max_length=100, help_text='Шаги приготовления')
    time = forms.DecimalField(max_digits=5, decimal_places=0, help_text='Время приготовления (n часов)')
    pic = forms.ImageField(help_text='Изображение')
    tm = forms.TextInput(default='', max_length=100,help_text='Автор')