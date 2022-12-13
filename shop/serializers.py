import os
from rest_framework import serializers
from shop.models import Product
from django.conf import settings


class ProductDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = Product
        fields = '__all__'

    def get_image(self, obj):

        if obj.image:
            ext_list = []
            name = obj.image.name.split(".")[0]
            webp = os.path.join(settings.MEDIA_ROOT, f"{name}.webp")

            if os.path.exists(webp):
                ext_list.append("webp")

            path, ext = obj.image.url.split(".")
            ext_list.append(ext)
            try:
                data = {
                    'path': path,
                    'formats': ext_list
                }
                return data
            except Exception:
                return None
        else:
            return None
