
import os
import sys

import django

from django.conf import ENVIRONMENT_VARIABLE
from django.core import management

os.environ[ENVIRONMENT_VARIABLE] = 'manejalo.settings'

management.call_command('test', 'app')
