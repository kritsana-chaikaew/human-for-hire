from django.forms import ModelForm, Textarea
from .models import Product

class EditPostForm(ModelForm):

    class Meta:
        model = Product
        fields = (
            'product_name',
            'product_image',
            'product_details',
            'start_date',
            'end_date',
            'location',
            'tags',
        )
        labels = {
            'product_image': 'Picture',
            'product_details': 'Description',
            'start_date': 'Start date and time',
            'end_date': 'End date and time',
            'tags': 'Tag'
        }
        widgets = {
            'product_details': Textarea(attrs={'rows': 3})
        }

    def save(self, commit=True):
        product = super(EditPostForm, self).save(commit)
        if commit:
            product.save()
        return product
