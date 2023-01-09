from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm
from django.forms import NumberInput, Select


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'gender',
            'target',
            'age',
            'height',
            'weight',
        )


class UserUpdateForm(ModelForm):
    
    class Meta:
        model = User
        fields = (
            'gender',
            'target',
            'age',
            'height',
            'weight',
        )
        labels = {
            'gender': 'Пол',
            'target': 'Цель',
            'age': 'Возраст',
            'height': 'Высота',
            'weight': 'Вес',
        }
        widgets = {
            'age': NumberInput(attrs={'class': 'field'}),
            'height': NumberInput(attrs={'class': 'field'}),
            'weight': NumberInput(attrs={'class': 'field'}),
            'gender': Select(attrs={'class': 'field'}),
            'target': Select(attrs={'class': 'field'}),
        }