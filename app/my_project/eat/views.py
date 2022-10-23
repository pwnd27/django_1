from django.shortcuts import render


# Create your views here.
def to_eat(request):
    return render(request, 'eat/index.html')
