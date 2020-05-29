from django import forms
from .models import Product

from django.utils.text import slugify

PUBLISH_CHOISES = (
    #('', ""),
    ('publish', "Publish"),
    ('draft', "Draft"),
)

class ProductModelForm(forms.ModelForm):
    tags = forms.CharField(label='Related tags', required=False)
    publish = forms.ChoiceField(widget=forms.RadioSelect,choices=PUBLISH_CHOISES, required=False)
    # title = forms.CharField(label='Your Title', widget=forms.TextInput(
    #     attrs={
    #         "class":"custom-class",
    #         "placeholder":"Title",
    #     }
    # ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "class":"my-custom-class",
            "placeholder":"Description",
            "some-attr":"this"
        }
    ))
    price = forms.DecimalField()

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
        ]

    def clean(self, *args, **kwargs):
        cleaned_data = super(ProductModelForm, self).clean(*args, **kwargs)
        #title = cleaned_data.get("title")
        # slug = slugify(title)
        # qs = Product.objects.filter(slug=slug).exists()
        # if qs:
        #     raise forms.ValidationError("Title is taken, new title is needed. Please try again")
        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 1.00:
            raise forms.ValidationError("Price must be greater than $1,00")
        elif price >= 100.00:
            raise forms.ValidationError("Price must be less than $100,00")
        else:
            return price

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) > 3:
            return title
        else:
            raise forms.ValidationError("Title must be greater than 3 characteers long.")
