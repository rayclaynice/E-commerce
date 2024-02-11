from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.admin import UserAdmin



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


        
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)   #super().__init__(name)  super(<YourModelName>, self).__init__(*args, **kwargs) 
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


        #email validation

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():  #filters the available users and if its equal to the one it input field it raises a validation error 
            raise forms.ValidationError('this email is invalid')
        if len(email) >= 350:
            raise forms.ValidationError("your email is too long")
        return email