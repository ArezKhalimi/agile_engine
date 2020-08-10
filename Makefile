run-beat:
	celery -A agile beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
run-celery:
	celery -A agile  worker --loglevel=info
build:
	cp .env.example .env && \
	pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt && \
	python manage.py migrate && \
	python manage.py create_scheduler
