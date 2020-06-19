from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'city', 'address', 'phone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].widget.attrs['class'] = 'sizefull s-text7 p-l-15 p-r-15'
            self.fields[field].widget.attrs['placeholder'] = field