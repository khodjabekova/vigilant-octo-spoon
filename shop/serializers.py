from rest_framework import serializers
from shop.models import Product


class ProductDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = Product
        fields = '__all__'


    def get_image(self, obj):

        if obj.image:
            path, format = obj.image.url.split(".")
            try:
                data = {
                    'path': path,
                    'formats': [format]

                }
                return data
            except Exception:
                return None
        else:
            return None