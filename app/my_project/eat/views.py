from django.shortcuts import render
from .models import GeneratedMeals


# Create your views here.
def show_diet(request):

    return render(request, 'eat/index.html')
