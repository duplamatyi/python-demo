from common_settings import *

DEBUG = True
TEMPLATE_DEBUG = True

INTERNAL_IPS = [
    '127.0.0.1'
]

INSTALLED_APPS += [
    'debug_toolbar',
]
