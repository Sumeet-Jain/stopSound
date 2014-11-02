from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    is_active = models.BooleanField(default=False)

    def send_text(self, voice):
        voice.send_sms(str(self.phone_number), "Dear %s, Stop Sound is giving you a sound warning" % self.name)

class Settings(models.Model):
    name = models.CharField(max_length=100)
    sound_level = models.FloatField()
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_active:
            try:
                temp = Settings.objects.get(is_active=True)
                if self != temp:
                    temp.is_active = False
                    temp.save()
            except Settings.DoesNotExist:
                pass
        super(Settings, self).save(*args, **kwargs) 
