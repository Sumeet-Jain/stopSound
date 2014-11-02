from django.core.management.base import BaseCommand
from contacts.models import Settings

class Command(BaseCommand):
    help = 'Creates three initial sound settings'

    def handle(self, *args, **options):
        Settings.objects.create(name="Sensitive", sound_level=50, is_active=True)
        self.stdout.write('Created Sensitive Setting')
        Settings.objects.create(name="Sorta Sensitive", sound_level=100, is_active=True)
        self.stdout.write('Created Middle Sensitive Setting')
        Settings.objects.create(name="Not Sensitive", sound_level=500, is_active=True)
        self.stdout.write('Created Not Sensitive Setting')
