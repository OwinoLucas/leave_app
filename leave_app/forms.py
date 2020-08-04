from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Employee


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=60, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'email']


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['id_number', 'date_of_employment', 'gender', 'department', 'profile_pic', 'phone_number', 'blood_group', 'marital_status', 'address']