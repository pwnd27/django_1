from django.shortcuts import render
from django.db.models import Sum
from .models import Meal, User, MealPlan
from .forms import UserForm, UserUpdateForm


def calc_calories(user):
    
    calories = 0
    weight = user.cleaned_data['weight']
    height = user.cleaned_data['height']
    age = user.cleaned_data['age']
    if user.cleaned_data['gender'] == 0:
        calories = ((10 * weight) + (6.25 * height) - (5 * age) - 161) * 1.3
    else:
        calories = ((10 * weight) + (6.25 * height) - (5 * age) + 5) * 1.375

    if user.cleaned_data['target'] == 'G':
        calories += 300
    elif user.cleaned_data['target'] == 'L':
        calories -= 300

    return calories



def signup(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])

            calories = calc_calories(user_form)
            
            mealplan = MealPlan.objects.get(calories__contains=str(calories)[:2])
            new_user.meal_plan = mealplan

            new_user.save()
            return render(request, 'registration/registration_done.html', {'new_user': new_user})
    user_form = UserForm()
    return render(request, 'registration/signup.html', {'form': user_form})


def update_user(request):

    username = request.user.get_username()
    user = User.objects.get(username=username)
    
    if request.method == 'POST':
        bound_form = UserUpdateForm(request.POST, instance=user)        
        if bound_form.is_valid():
            calories = calc_calories(bound_form)
            mealplan = MealPlan.objects.get(calories__contains=str(calories)[:2])
            new_user.meal_plan = mealplan
            new_user = bound_form.save()
            return render(request, 'registration/update_user.html', {'form': bound_form, 'user': new_user})
    
    else:
        bound_form = UserUpdateForm(instance=user)
        return render(request, 'registration/update_user.html', {'form': bound_form, 'user': user})



def show_diet(request):
    

    if request.user.is_authenticated:
        
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
    else:
        return render(request, 'diet/static_diet.html')

def show_ingredients(request):
    
    ingredients = Meal.objects.select_related('ingredient')
    return render(request, 'diet/ingredients.html', context={'ingredients': ingredients})