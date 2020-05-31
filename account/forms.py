from django import forms
from django.contrib.auth.hashers import make_password
from account.models import User


class RegistrationForm(forms.ModelForm):
    password_confirm = forms.CharField(
        widget=forms.PasswordInput, label='повторить пароль'
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }
        labels = {
            "password": 'пароль',
            'username': 'телефон',
            'first_name': 'имя'
        }
        help_texts = {
            'username': 'пример 375291234567',
        }

    def clean(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if password != password_confirm:
            raise forms.ValidationError('пароль не совпал')
        if len(password) < 5:
            raise forms.ValidationError('короткий пароль')
        if not password.isalnum():
            raise forms.ValidationError('в пороле допускаються только цифры и буквы')
        return self.cleaned_data

    def clean_username(self):
        username = self.data['username']
        if not username.isdigit() or not len(username) == 12:
            raise forms.ValidationError('недопустимое имя')
        return username

    def save(self, commit=True):
        self.instance.password = make_password(self.cleaned_data['password'])
        return super().save(self)


class VerificationForm(forms.Form):
    token = forms.CharField(
        label='секретный ключ'
    )

    def clean_token(self):
        token = self.data['token']
        if not token.isdigit() or not len(token) == 6:
            raise forms.ValidationError('недопустимые символы')
        return self.data['token']


class LoginForm(forms.Form):
    login = forms.CharField(
        label='телефон'
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='пароль'
    )

    def clean_login(self):
        login = self.data['login']
        if not login.isdigit() or not len(login) == 12:
            raise forms.ValidationError('недопустимые символы')
        return self.data['login']


class ChangePasswdForm(forms.ModelForm):
    password_confirm = forms.CharField(
        widget=forms.PasswordInput, label='повторить пароль'
    )

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }
        labels = {
            "password": 'пароль',
            'username': 'телефон',
        }
        help_texts = {
            'username': 'пример 375291234567',
        }

    def clean(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if password != password_confirm:
            raise forms.ValidationError('пароль не совпал')
        if len(password) < 5:
            raise forms.ValidationError('короткий пароль')
        if not password.isalnum():
            raise forms.ValidationError('в пороле допускаються только цифры и буквы')
        self.instance.password = make_password(self.cleaned_data['password'])
        return self.cleaned_data

