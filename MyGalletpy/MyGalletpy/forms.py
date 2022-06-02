from django import forms

class RegisterForm(forms.Form):
    username_field = forms.CharField(label='username_field', max_length=30, min_length=1, required=True)
    password_field = forms.CharField(label='password_field', max_length=50, min_length=1, required=True)
    password_repeat_field = forms.CharField(label='password_repeat_field', max_length=50, min_length=1, required=True)

class LoginForm(forms.Form):
    username_field_login = forms.CharField(label='username', max_length=30, min_length=1, required=True)
    password_field_login = forms.CharField(label='password', max_length=50, min_length=1, required=True)

class TransactionForm(forms.Form):
    transaction_amount = forms.CharField()
    transaction_reason = forms.CharField()
    transaction_date = forms.CharField()
    transaction_type = forms.CharField()
    transaction_behavior = forms.CharField()
    transaction_pocket = forms.CharField()

class PocketCreationForm(forms.Form):
    pocket_creation_name = forms.CharField()