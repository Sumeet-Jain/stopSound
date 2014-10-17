import os

from django.db import models
from googlevoice import Voice
from phonenumber_field.modelfields import PhoneNumberField

EMAIL = os.environ.get('GV_EMAIL')
PASSWORD = os.environ.get('GV_PW')
voice = Voice()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    is_active = models.BooleanField(default=False)

    def send_text(self):
        voice.login(email=EMAIL, passwd=PASSWORD)
        voice.send_sms(str(self.phone_number), "Dear %s, Stop Sound says: SHUT THE FUCK UP" % self.name)

class Settings(models.Model):
    sound_level = models.IntegerField()
