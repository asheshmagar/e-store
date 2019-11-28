from django import forms  
from product.models import Product, Color, Size

class ProductForm(forms.ModelForm):  
    # pimage = forms.ImageField()
    pcolor = forms.ModelMultipleChoiceField(
        queryset=Color.objects.values_list('color', flat=True),
        widget=forms.CheckboxSelectMultiple
    )
    psize = forms.ModelMultipleChoiceField(
        queryset=Size.objects.values_list('size', flat=True),
        widget=forms.CheckboxSelectMultiple
    )


    class Meta:  
        model = Product 
        fields = "__all__"
        labels = {
            'pcolor': 'Colors'
        }