import sys
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image

def compressImageToWebp(image):

    try:
        im = Image.open(image)
        im.verify()
    except Exception:
        return None

    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, format='WEBP', optimize=True, quality=50)
    webp = InMemoryUploadedFile(im_io, 'ImageField', "%s.webp" % image.name.split(
        '.')[0], 'image/webp', sys.getsizeof(image), None)
    return webp