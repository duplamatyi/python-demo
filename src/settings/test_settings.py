from common_settings import *

DEBUG = False
TEMPLATE_DEBUG = False

INTERNAL_IPS = [
    '127.0.0.1'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'python_demo_test',
    }
}

# ----------------- SELENIUM ----------------------
SELENIUM_DRIVER = 'Firefox'
SELENIUM_DISPLAY = ":99.0"
