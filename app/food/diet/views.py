from django.shortcuts import render
from django.db.models import Sum
from .models import Meal, Ingredient



def show_diet(request):
    
    meals = Meal.objects.values('meal_name__name', 'meal_name__time').\
        annotate(calories=Sum('ingredient__calories'), weigth=Sum('ingredient_weigth'), \
        fats=Sum('ingredient__fats'), proteins=Sum('ingredient__proteins'), carbs=Sum('ingredient__carbs'))
    
    breakfast = meals.filter(meal_name__time='M')
    lunch = meals.filter(meal_name__time='A')
    supper = meals.filter(meal_name__time='E')
    info = meals.aggregate(Sum('calories'), Sum('fats'), Sum('proteins'), Sum('carbs'))

    context = {
        'breakfast': breakfast,
        'lunch': lunch,
        'supper': supper,
        'info': info
    }

    return render(request, 'diet/index.html', context=context)

def show_ingredients(request):
    
    ingredients = Ingredient.objects.all()

    return render(request, 'diet/ingredients.html', context={'ingredients': ingredients})