from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agile.settings')

app = Celery(
    'agile',
    broker='amqp://guest:guest@localhost//',
    include=[
        'agile.apps.images.tasks',
    ]
)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update({
    'task_acks_late': True,
})

# app.conf.task_routes = ([
#     (
#         'agile.apps.images.tasks',
#         {
#             'queue': 'queue_periodic_tasks',
#             'routing_key': 'queue_periodic_tasks'
#         }
#     ),
# ],)
