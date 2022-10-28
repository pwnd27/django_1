from tabnanny import verbose
from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    calories = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    carbs = models.FloatField()

    def __str__(self):
        return f'{self.name}'


class MealName(models.Model):
    MORNING = 'M'
    AFTERNOON = 'A'
    EVENING = 'E'
    MEAL_TIME = (
        (MORNING, 'morning'),
        (AFTERNOON, 'afternoon'),
        (EVENING, 'evening'),
    )
    name = models.CharField(max_length=50, db_index=True)
    time = models.CharField(max_length=1, choices=MEAL_TIME, db_index=True)

    def __str__(self):
        return f'{self.name}'



class Meal(models.Model):
    meal_name = models.ForeignKey(MealName, on_delete=models.DO_NOTHING, db_index=True, verbose_name='meal_name')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.DO_NOTHING, db_index=True, verbose_name='ingredient')
    ingredient_weigth = models.FloatField()

    def __str__(self):
        return f'{self.meal_name}'


# class GeneratedMeals(models.Model):
#     meal_name = models.ForeignKey(MealName, on_delete=models.DO_NOTHING, db_index=True)

#     def __str__(self):
#         return f'{self.meal_name}'
