from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.messages import constants
from django.forms.utils import ErrorList
from django.utils.html import format_html, format_html_join
from restaurante_beira.settings import MESSAGE_TAGS

from accounts.models import User


class DivErrorList(ErrorList):
    def as_div(self):
        if not self:
            return ''
        return format_html(
            '<div>{}</div>',
            format_html_join(
                '', '<div class="alert {}" role="alert">{}</div>',
                ((MESSAGE_TAGS[constants.ERROR], error) for error in self)
            )
        )

    def __str__(self):
        return self.as_div()


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auto_id = '%s'
        self.error_class = DivErrorList


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
        self.error_class = DivErrorList
