from django import forms
from groceryapp.models import supermarket

class supermarketForm(forms.ModelForm):
    class Meta:
        model = supermarket
        fields = '__all__'
        #['productname','productid','price','Quantityinhand','soldquantity','Remainingstock']