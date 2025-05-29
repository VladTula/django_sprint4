from django.contrib.auth.forms import UserCreationForm
from users.models import MyUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ('username', 'bio')
