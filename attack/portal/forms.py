from django import forms

class LoginForm(forms.Form):

    employeeNumber = forms.CharField(
        label='Employee Number',
        max_length=8,
        required=True,
        widget=forms.TextInput()
    )

    inputPassword = forms.CharField(
        label='Your Password',
        max_length=256,
        min_length=6,
        required=True,
        widget=forms.PasswordInput()
    )


