from django.utils.html import format_html, format_html_join
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.utils import ErrorList
# from restaurante_beira.settings import MESSAGE_TAGS
# from django.contrib.messages import constants


# class DivErrorList(ErrorList):
#     def as_div(self):
#         if not self:
#             return ''
#         return format_html(
#             '<div>{}</div>',
#             format_html_join(
#                 '', '<div class="alert {}" role="alert">{}</div>',
#                 ((MESSAGE_TAGS[constants.ERROR], error) for error in self)
#             )
#         )

#     def __str__(self):
#         return self.as_div()


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auto_id = '%s'
        # self.error_class = DivErrorList


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
        # self.error_class = DivErrorList
