from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from googlevoice import Voice

voice = None

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    is_active = models.BooleanField(default=False)

    def send_text(self):
        global voice
        if not voice:
            voice = Voice()
            voice.login()
        voice.send_sms(self.phone_number, "You have been notified by stop sound to shut up")

class Settings(models.Model):

    sound_level = models.IntegerField()
