import json

from .forms import ContactForm
from .models import Contact, Settings

from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

only_superuser_decorator = user_passes_test(lambda u: u.is_superuser)

def serialize_settings(request):
    settings = Settings.objects.filter(is_active=True)
    resp = {'sound_level': settings.sound_level}
    return HttpResponse(json.dumps(resp), content_type="application/json")

@only_superuser_decorator
def send_messages(request):
    contacts = Contact.objects.filter(is_active=True)
    for contact in contacts:
        contact.send_text()
    resp = {'success': True}
    return HttpResponse(json.dumps(resp), content_type="application/json")

def contacts(request):
    all_contacts = Contact.objects.all()
    context = {
        'contacts': all_contacts,
    }
    
    return render(request, 'contacts/view_all.html', context)

def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a new contact')
            return HttpResponse('Success')
    else:
        form = ContactForm()

    return render(request, 'contacts/add_contact.html', {'form': form})
