from django import forms
from .models import Product

class EditPostForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'product_name',
            'product_image',
            'product_details',
            'price',
            'start_date',
            'end_date',
            'location',
            'tags',
        )

    def save(self, commit=True):
        product = super(EditPostForm, self).save(commit)
        if commit:
            product.save()
        return product
