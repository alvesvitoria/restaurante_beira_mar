from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from accounts.models import User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auto_id = '%s'


class RegisterForm(UserCreationForm):
    class Meta:
        # exclude = ()
        model = User
        fields = ('first_name', 'last_name', 'cpf', 'birth_date',
                  'email', 'phone')

    field_order = [
        'first_name',
        'last_name',
        'birth_date',
        'phone',
        'cpf',
        'email',
        'password1',
        'password2',
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auto_id = '%s'
