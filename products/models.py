from loguru import logger

from django.db import models
from django.db.models.signals import post_save

from utils.utils import flip_image

logger.add('model_debug.log', format='{time} {level} {message}', level='DEBUG', rotation="14:00", compression='zip')

class Product(models.Model):
    modified = models.BooleanField(default=False)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=100, null=False)
    uuid = models.CharField(max_length=10, null=False, unique=True, primary_key=True)
    logo = models.ImageField(upload_to='images/', null=True, blank=True, default='images/default.png')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True, blank=True, null=True)
    rotate_duration = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    @logger.catch
    def save(self, *args, **kwargs):
        uuid = self.uuid
        super(Product, self).save(*args, **kwargs)
        logger.info(f'New product object {uuid}')

def update_rotate_duration(sender, instance, **kwargs):
    """
    flipping logo image every time after uploading on server (update/create post)
    """

    if instance.logo:
        post_save.disconnect(update_rotate_duration, sender=sender)
        instance.rotate_duration = flip_image(instance.logo)  # flip_image returns function operation time
        instance.save()
        post_save.connect(update_rotate_duration, sender=sender)

        logger.info(f'Product {instance.uuid} rotate image duration: {instance.rotate_duration}')

post_save.connect(update_rotate_duration, sender=Product)
