import json

from .forms import ContactForm
from .models import Contact, Settings

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def only_superuser(func):
    def inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseRedirect(reverse('access_denied'))
        return func(request, *args, **kwargs)
    return inner

def serialize_settings(request):
    settings = Settings.objects.filter(is_active=True)
    resp = {'sound_level': settings.sound_level}
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
@only_superuser
def send_messages(request):
    if request.method == "POST":
        contacts = Contact.objects.filter(is_active=True)
        for contact in contacts:
            contact.send_text()
        messages.success(request, "Sent messages to all active members")
    return HttpResponseRedirect(reverse('before_send_messages'))

@login_required
@only_superuser
def before_send_messages(request):
    return render(request, "contacts/send_messages.html")

@login_required
def contacts(request):
    all_contacts = Contact.objects.all()
    context = {
        'contacts': all_contacts,
    }
    
    return render(request, 'contacts/view_all.html', context)

@login_required
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

@login_required
def edit_contact(request, id_):
    # Consider merging above and this view
    contact = Contact.objects.get(pk=id_)

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited a contact')
            return HttpResponse('Success')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contacts/add_contact.html', {'form': form})

