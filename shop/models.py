import os

from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from imagekit.models import ProcessedImageField
from django.conf import settings
from config.util import compressImageToWebp
from PIL import Image

# Create your models here.
class Product(models.Model):
    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

        ordering = ['title']

    IN_STOCK = 1
    ON_REQUEST = 2
    EXPECTED = 3
    NOT_AVAILABLE = 4
    NOT_PRODUCED = 5

    STATUS_CHOICE = (
        (IN_STOCK, 'В наличии'),
        (ON_REQUEST, 'Под заказ'),
        (EXPECTED, 'Ожидается поступление'),
        (NOT_AVAILABLE, 'Нет в наличии'),
        (NOT_PRODUCED, 'Не производится'),
    )

    title = models.CharField(_('title'), max_length=255)
    sku = models.CharField(_('sku'), max_length=255, unique=True)
    price = models.IntegerField(_('price'))
    status = models.PositiveSmallIntegerField(_('status'),
        choices=STATUS_CHOICE, null=True, blank=True)
    image = models.ImageField(_('image'), upload_to='images', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=["jpg", "png"])])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.image:
            # webp = compressImageToWebp(self.image)
            image = Image.open(self.image)
            name = self.image.name.split(".")[0]
            path = os.path.join(settings.MEDIA_ROOT, 'images')
            image.save(f"{path}/{name}.webp")
        super(Product, self).save(*args, **kwargs)