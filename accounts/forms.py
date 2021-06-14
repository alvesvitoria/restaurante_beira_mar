from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from accounts.models import Cliente


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auto_id = '%s'


class RegisterForm(UserCreationForm):
    class Meta:
        # exclude = ()
        model = Cliente
        fields = ('first_name', 'last_name', 'cpf', 'birth_date',
                  'email', 'phone_number')

    field_order = [
        'first_name',
        'last_name',
        'birth_date',
        'phone_number',
        'cpf',
        'email',
        'password1',
        'password2',
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auto_id = '%s'
