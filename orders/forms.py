from django import forms
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from account.models import ShopUser
from .models import Order

class PhoneVerificationForm(forms.Form):
    phone = forms.CharField(max_length=11, label='شماره موبایل' , required=True, widget=forms.TextInput(attrs={
            'placeholder': 'مثال: 0912xxxxxxx',
            'class': 'form-control',
            'dir': 'ltr'}))
    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        if len(phone) < 11:
            raise forms.ValidationError('1234')

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'address',
                  'postal_code', 'province', 'city']
