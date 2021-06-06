from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from .validators import cpf_validator


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    # nome, cpf, sexo, data de nascimento, email, telefone e senha

    first_name = models.CharField('primeiro nome', max_length=150, null=True)

    last_name = models.CharField('último nome', max_length=150, null=True)

    cpf = models.CharField('CPF', max_length=13, null=False,
                           validators=[MinLengthValidator(11), cpf_validator])

    birth_date = models.DateField('data de nascimento', null=True)

    email = models.EmailField('email', validators=[
                              validate_email], unique=True)

    phone = models.CharField('telefone', max_length=30, null=False)

    date_joined = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False, help_text=_(
        'Designates whether the user can log into this admin site.'))

    objects = UserManager()

    # REQUIRED_FIELDS = ['email']

    USERNAME_FIELD = 'email'
