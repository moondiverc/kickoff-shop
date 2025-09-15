from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "stock", "description", "category", "thumbnail", "rating", "is_featured"]