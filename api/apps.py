from __future__ import unicode_literals

from django.apps import AppConfig
from .models import ForgotPassOp


class ApiConfig(AppConfig):
    name = 'api'
