from django.contrib.auth.models import AbstractUser
from django.db import models


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


class GeneratedMeals(models.Model):
    meal_name = models.ForeignKey(MealName, on_delete=models.DO_NOTHING, db_index=True)

    def __str__(self):
        return f'{self.meal_name}'


class MealPlan(models.Model):
    calories = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    carbs = models.FloatField()
    gen_meals = models.ForeignKey(GeneratedMeals, on_delete=models.DO_NOTHING, db_index=True, null=True)

        
class User(AbstractUser):
    GENDER_CHOICES = (
        (0, 'FEMALE'),
        (1, 'MALE')
    )
    TARGET_CHOICES = (
        ('L', 'LOSE'),
        ('S', 'STABLE'),
        ('G', 'GAIN')
    )
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True, default=0)
    target = models.CharField(max_length=1, choices=TARGET_CHOICES, null=True)
    age = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.DO_NOTHING, null=True, db_index=True)

    def __str__(self):
        return self.username


class Ingredient(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    calories = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    carbs = models.FloatField()

    def __str__(self):
        return f'{self.name}'


class Meal(models.Model):
    meal_name = models.ForeignKey(MealName, on_delete=models.DO_NOTHING, db_index=True, verbose_name='meal_name')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.DO_NOTHING, db_index=True, verbose_name='ingredient')
    ingredient_weigth = models.FloatField()

    def __str__(self):
        return f'{self.meal_name}'

