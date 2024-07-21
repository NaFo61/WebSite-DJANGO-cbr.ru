from django.forms import ModelForm
from .models import Order
from django import forms
from .models import CustomUser, Review
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        label='Юзернейм',
        widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(
        max_length=254
    )
    phone_number=forms.CharField(
        max_length=30,
        required=True,
        label='Номер телефона',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    address = forms.CharField(
        max_length=300,
        required=True,
        label='Адрес',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )
    password2 = forms.CharField(
        label='Повтор пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.phone_number = self.cleaned_data['phone_number']
        user.address = self.cleaned_data['address']
        if commit:
            user.save()
        return user


class ReviewForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"})
    )

    class Meta:
        model = Review
        fields = ["text"]
