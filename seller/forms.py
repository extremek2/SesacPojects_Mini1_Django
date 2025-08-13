from django import forms
from products.models import Products
from seller.models import Seller


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name','category', 'price', 'quantity', 'uploaded_image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'uploaded_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['sellerName', 'store_name', 'phone_number', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }
