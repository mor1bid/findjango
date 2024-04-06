from django import forms

class RecipeForm(forms.Form):
    rec = forms.DecimalField(label='Номер рецепта')
    name = forms.CharField(label='Название блюда', required=False)
    desc = forms.CharField(label='Описание', required=False)
    steps = forms.CharField(label='Шаги приготовления', required=False)
    time = forms.DecimalField(label='Время приготовления (n часов)', required=False)
    pic = forms.ImageField(label='Изображение', required=False)
    tm = forms.CharField(label='Автор', required=False)