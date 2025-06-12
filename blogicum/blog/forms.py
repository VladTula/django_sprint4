from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment

User = get_user_model()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        exclude = ()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ()


class PasswordChangeForm(forms.Form):
    password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm new password', widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
