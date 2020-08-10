from django.core.management.base import BaseCommand

from django_celery_beat.models import PeriodicTask, IntervalSchedule


INTERVALS = (
    IntervalSchedule.DAYS,
    IntervalSchedule.HOURS,
    IntervalSchedule.MINUTES,
    IntervalSchedule.SECONDS,
    IntervalSchedule.MICROSECONDS,
)


class Command(BaseCommand):
    help = 'Bind viber endpoints'

    def add_arguments(self, parser):
        parser.add_argument(
            '-t', '--time', type=int, default=10
        )
        parser.add_argument(
            '-i', '--interval', type=str, default=IntervalSchedule.MINUTES
        )

    def handle(self, *args, **options):
        time = options['time']
        interval = options['interval']
        if interval not in INTERVALS:
            raise ValueError(f'Only {INTERVALS} intervals are avaliable')

        schedule, created = IntervalSchedule.objects.get_or_create(
            every=time,
            period=interval,
        )

        PeriodicTask.objects.get_or_create(
            interval=schedule,
            name='Update cache',
            task='agile.apps.images.tasks.update_image_data',
        )
        self.stdout.write(self.style.SUCCESS('Successfully set new scheduler'))
