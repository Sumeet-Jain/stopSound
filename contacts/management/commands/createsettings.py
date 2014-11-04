from django.core.management.base import BaseCommand
from contacts.models import Settings

class Command(BaseCommand):
    help = 'Creates three initial sound settings'

    def handle(self, *args, **options):
        Settings.objects.all().delete()
        sensitive_name = "Sensitive -- monitors sound near ambient threshold. Use for quiet study sessions."
        sorta_name = "Sort of Sensitive -- monitors sound about 1.5 times the ambient threshold. Use for medium situations."
        not_name = "Insensitive -- monitors sound about 2.0 times the ambient threshold. Use for loud situations."
        Settings.objects.create(name=sensitive_name, sound_level=1.05, is_active=True)
        self.stdout.write('Created Sensitive Setting')
        Settings.objects.create(name=sorta_name, sound_level=1.5, is_active=False)
        self.stdout.write('Created Middle Sensitive Setting')
        Settings.objects.create(name=not_name, sound_level=2.0, is_active=False)
        self.stdout.write('Created Not Sensitive Setting')
