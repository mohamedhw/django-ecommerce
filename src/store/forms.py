from django import forms
from django_countries.fields import CountryField

PAYMENT_OPTIONS = (
    ('credit card', 'credit card'),
    ('debit card', 'debit card'),
    ('paypal', 'paypal'),
)

class CheckoutForm(forms.Form):
    address = forms.CharField()
    address2 = forms.CharField(required=False)
    country = CountryField(blank_label='(select country)').formfield(attrs={
        'class': 'custom-select d-block w-100'
    })
    zip = forms.CharField()
    same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect,choices=PAYMENT_OPTIONS)