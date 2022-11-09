from django.urls import path
from .views import *

urlpatterns = [
    path('', show_diet, name='diet_url'),
    path('ingredients/', show_ingredients, name='ingredients_url'),
]