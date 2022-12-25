from django.forms import  ModelForm
from .models import Customuser


class RegisterForm(ModelForm):
    class Meta:
        model = Customuser
        fields = ['username', 'email', 'password', 'phone_number',]
        
        
class ForgotPwdForm(ModelForm):
    class Meta:
        model = Customuser
        fields = [ 'email', ]
        
        
class LoginForm(ModelForm):
    class Meta:
        model = Customuser
        fields = ['email', 'password']
        
        

