from django import forms
from .models import Product

class ProductFilterForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'color', 'price_from', 'price_to']

    CATEGORY_CHOICES = [(category, category) for category in Product.objects.values_list('category', flat=True).distinct()] + [('', 'All Categories')]
    COLOR_CHOICES = [(color, color) for color in Product.objects.values_list('color', flat=True).distinct()] + [('', 'All Colors')]

    price_from = forms.DecimalField(required=False)
    price_to = forms.DecimalField(required=False)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False)
    color = forms.ChoiceField(choices=COLOR_CHOICES, required=False)

class ProductSearchForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name']

    name = forms.CharField(max_length=100, required=False,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Search product..'}))