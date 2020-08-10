from agile.apps.images.utils import ImageStorageHandler
from agile.celery import app


@app.task()
def update_image_data():
    handler = ImageStorageHandler()
    handler.update_image_cache()
