from celery.schedules import crontab


#Schedule daily imports at midnight
CELERYBEAT_SCHEDULE = {
    'import-hotels': {
        'task': 'src.apps.hotel.tasks.import_cities',
        'schedule': crontab(minute=0, hour=0),
        'args': ()
    },
}

CELERY_TIMEZONE = 'UTC'
