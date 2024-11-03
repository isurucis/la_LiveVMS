from django import forms
from products.models import  Product
from .models import CampaignProduct

class CampaignProductForm(forms.ModelForm):
    class Meta:
        model = CampaignProduct
        fields = ['product']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Start with all active products
        self.fields['product'].queryset = Product.objects.filter(is_active=True, stock__gt=0)

        # Optionally, filter by category if a category is passed
        category_id = kwargs.get('initial', {}).get('category_id')
        if category_id:
            self.fields['product'].queryset = self.fields['product'].queryset.filter(category_id=category_id)
