import json

from django.db import models
from googlevoice import Voice
from phonenumber_field.modelfields import PhoneNumberField

voice = Voice()
with open('../screct_creds.json', 'r') as f_:
    secrets = json.load(f_)
    EMAIL = secrets['email']
    PASSWORD = secrets['pw']

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    is_active = models.BooleanField(default=False)

    def send_text(self):
        voice.login(email=EMAIL, passwd=PASSWORD)
        voice.send_sms(str(self.phone_number), "You have been notified by stop sound to shut up")

class Settings(models.Model):

    sound_level = models.IntegerField()
