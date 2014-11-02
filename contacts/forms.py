from .models import Contact, Settings

from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'is_active']

class ChooseASettingForm(forms.Form):
    CHOICES = tuple(((setting.pk, setting.name) for setting in Settings.objects.all()))
    choice = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
