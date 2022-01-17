import os
import time

from PIL import Image
from django.conf import settings


def flip_image(obj):
    start_time = time.time()
    path = settings.MEDIA_ROOT
    path = (path.replace(os.sep, '/') + f'/{obj}')
    im = Image.open(path)
    out = im.rotate(180)
    out.save(path)
    return time.time() - start_time
