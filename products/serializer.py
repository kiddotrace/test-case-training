from rest_framework import serializers
from products.models import Product


class BaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

class ProductListSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        exclude = ['created', 'updated', 'rotate_duration']


class ProductCreateSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):

        exclude = ['created', 'updated', 'rotate_duration', 'modified']


class ProductUpdateSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        exclude = ['created', 'updated', 'rotate_duration', 'uuid']

    def validate(self, attrs):
        if attrs['modified']:

            raise serializers.ValidationError('You have already edit this product')
        attrs['modified'] = True
        return attrs
