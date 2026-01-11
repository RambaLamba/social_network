from django import forms
from .models import Image, Profile, Publication
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('title', 'text', 'image')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=35, label='Имя')
    last_name = forms.CharField(max_length=35, label='Фамилия')
    email = forms.EmailField(required=False, label='Email')
    age = forms.IntegerField(required=False, label='Возраст')
    MARITAL_STATUS = [('Женат/замужем', 'Женат/замужем'),
                      ('Не женат/Не замужем', 'Не женат/Не замужем'),
                      ('В разводе', 'В разводе'),
                      ('Вдовец/Вдова', 'Вдовец/Вдова'),
                      ('Помолвлен/помолвлена', 'Помолвлен/помолвлена')]

    family_status = forms.ChoiceField(choices=MARITAL_STATUS, required=False, label='Выберите семейное положение')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'age', 'family_status' ,'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'age', 'family_status', 'bio']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

