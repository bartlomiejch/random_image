from django.db import models
from sorl.thumbnail import ImageField


class DummyImage(models.Model):
    image = ImageField(upload_to='static/images')
