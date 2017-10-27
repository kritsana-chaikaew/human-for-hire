from django import forms
from .models import Product

class EditPostForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'product_image',
            'product_name',
            'start_date',
            'end_date',
            'product_details',
            'location',
            'price',
            'tags',
        )

    def save(self, commit=True):
        product = super(EditPostForm, self).save(commit)
        if commit:
            product.save()
        return product
