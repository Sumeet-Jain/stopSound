import json
import os

from django.db import models
from googlevoice import Voice
from phonenumber_field.modelfields import PhoneNumberField

EMAIL = os.environ['GV_EMAIL']
PASSWORD = os.environ['GV_PW']

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    is_active = models.BooleanField(default=False)

    def send_text(self):
        voice.login(email=EMAIL, passwd=PASSWORD)
        voice.send_sms(str(self.phone_number), "You have been notified by stop sound to shut up")

class Settings(models.Model):

    sound_level = models.IntegerField()
