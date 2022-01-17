from django.forms import ModelForm, ValidationError, HiddenInput
from django_filters import FilterSet

from products.models import Product


class ProductBaseForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductListForm(ProductBaseForm):
    class Meta(ProductBaseForm.Meta):
        exclude = ['created', 'updated', 'rotate_duration']


class ProductCreateForm(ProductBaseForm):
    class Meta(ProductBaseForm.Meta):
        exclude = ['created', 'updated', 'rotate_duration', 'modified']


class ProductUpdateForm(ProductBaseForm):
    class Meta(ProductBaseForm.Meta):
        widgets = {
            'modified': HiddenInput(),
        }
        exclude = ['created', 'updated', 'rotate_duration']

    def clean_modified(self):
        """
        Allows to update the model only 1 time by using boolean field
        modified as a checker
        """
        modified = self.cleaned_data.get('modified')
        if modified:
            raise ValidationError('You have already edit this product')
        return True


class ProductFilter(FilterSet):
    class Meta(ProductBaseForm.Meta):
        model = Product
        fields = {
            'modified': ['exact'],
        }
