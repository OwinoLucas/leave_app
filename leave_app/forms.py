from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Employee, Leave


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

class UserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name', 'email']

class EmployeeCredentialsForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [ 'gender', 'department', 'phone_number']


class LeaveApplicationForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['start_date', 'end_date', 'leave_app']
