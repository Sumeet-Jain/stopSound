from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    is_active = models.BooleanField(default=False)

    def send_text(self, voice):
        voice.send_sms(str(self.phone_number), "Dear %s, Stop Sound says: SHUT THE FUCK UP" % self.name)

class Settings(models.Model):
    sound_level = models.IntegerField()
