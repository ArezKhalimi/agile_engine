CELERY_BROKER = env.str('CELERY_BROKER')
CELERY_TASK_ACKS_LATE = env.bool('CELERY_TASK_ACKS_LATE', default=True)