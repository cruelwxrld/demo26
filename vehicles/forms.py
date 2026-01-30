from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ 'name', 'price', 'supplier' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'supplier': forms.Select(attrs={'class': 'form-control'})
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'order_name', 'status', 'created_at',
            'updated_at', 'user', 'basket'
            ]
        widgets = {
            'order_name': forms.TextInput(),
            'status': forms.Select(),
            'created_at': forms.DateTimeBaseInput(),
            'updated_at': forms.DateTimeBaseInput(),
            'user': forms.Select(),
            'basket': forms.Select()
        }