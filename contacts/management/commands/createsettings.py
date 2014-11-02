from django.core.management.base import BaseCommand
from contacts.models import Settings

class Command(BaseCommand):
    help = 'Creates three initial sound settings'

    def handle(self, *args, **options):
        Settings.objects.all().delete()
        Settings.objects.create(name="Sensitive", sound_level=1.05, is_active=True)
        self.stdout.write('Created Sensitive Setting')
        Settings.objects.create(name="Sorta Sensitive", sound_level=1.5, is_active=True)
        self.stdout.write('Created Middle Sensitive Setting')
        Settings.objects.create(name="Not Sensitive", sound_level=2.0, is_active=True)
        self.stdout.write('Created Not Sensitive Setting')
