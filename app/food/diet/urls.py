from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('update/', update_user, name='update_user_url'),
    path('', show_diet, name='diet_url'),
    path('ingredients/', show_ingredients, name='ingredients_url'),
    path('accounts/', include('django.contrib.auth.urls')),
]