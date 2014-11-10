from .models import Contact, GlobalSettings, Settings

from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'is_active']

class ChooseASettingForm(forms.Form):
    CHOICES = tuple(((setting.pk, setting.name) for setting in Settings.objects.all()))
    choice = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

class ChooseAdvanceSettingForm(forms.Form):
    CHOICES = {
        'auto': 'Automate the threshold.',
        'auto-save': 'Automate once and save. Use until this option changes',
        'manual': 'Manually set choice',
    }
    CHOICES = CHOICES.items()
    choice = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)


class UpdateGlobalForm(forms.ModelForm):
    class Meta:
        model = GlobalSettings
        fields = ['sound_level']
