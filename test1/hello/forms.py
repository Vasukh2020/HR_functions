from django import forms 
from .models import Product



class ProductForm(forms.ModelForm):
    title = forms.CharField(label='',
              widget= forms.TextInput(attrs={"placeholder": "Enter title"}))
    
    description = forms.CharField(required=False,
    widget=forms.Textarea(
        attrs={
            "placeholder":"Description here",
            "class":"new",
            "id":"id-of-description",
            "rows":10,"cols":60
        }
    ))
    
    class Meta:
        model = Product
        fields=[
            'title',
            'description',
            'rating',
            'price'
            
        ]

class RawProductForm(forms.Form):
   title = forms.CharField()
   description = forms.CharField()
   price = forms.DecimalField()