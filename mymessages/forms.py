from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Message

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'nickname']

#新增user
#id: leon
#password: 5k4g4au4au83
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': '請輸入留言', 
                'class': 'form-control'
            })
        }
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser 
        fields = ['first_name', 'last_name', 'email', 'birthday', 'address', 'profile_picture']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }