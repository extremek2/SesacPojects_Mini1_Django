from django import forms
from .models import Order, OrderItem, Products

class OrderItemForm(forms.ModelForm):
    # product = forms.ModelChoiceField(
    #     queryset=Products.objects.filter(is_active=True).order_by('name'),
    #     label="Select Product"
    # )
    class Meta:
        model = OrderItem
        fields = ['product',
                  'quantity'
                  ]