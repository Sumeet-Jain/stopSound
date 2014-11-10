import json
import os

from .forms import ContactForm, ChooseAdvanceSettingForm, ChooseASettingForm, UpdateGlobalForm
from .models import Contact, GlobalSettings, Settings

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from twilio.rest import TwilioRestClient

def only_superuser(func):
    def inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseRedirect(reverse('access_denied'))
        return func(request, *args, **kwargs)
    return inner


def serialize_settings(request):
    settings = Settings.objects.get(is_active=True)
    global_settings = GlobalSettings.objects.all()[0]
    resp = {'sound_coefficent': settings.sound_level, 'name': settings.name}
    resp['threshold_method'] = global_settings.current_option
    resp['sound_level'] = global_settings.sound_level
    use_sound = ((global_settings.current_use_count and global_settings.current_option == 'auto-save') or
                global_settings.current_option == 'manual')
    resp['use_website_sound'] = use_sound
    resp['count'] = global_settings.current_use_count
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def update_settings(request):
    if request.method == "POST":
        global_settings = GlobalSettings.objects.all()[0]
        form = UpdateGlobalForm(request.POST, instance=global_settings)
        if form.is_valid():
            form.save()
            global_settings.current_use_count += 1
            global_settings.save()
            print "VALID FORM"
            messages.success(request, 'Successfully changed the sound settings')
    else:
        form = UpdateGlobalForm()

    return render(request, 'contacts/update_settings.html', {'form': form})


@login_required
@only_superuser
def send_messages_json(request):
    contacts = Contact.objects.filter(is_active=True)
    account_sid = os.environ['TWILIO_SID']
    auth_token = os.environ['TWILIO_TOKEN']
    twilio_number = os.environ['TWILIO_NUMBER']
    client = TwilioRestClient(account_sid, auth_token)
    for contact in contacts:
        message = client.messages.create(
            to=str(contact.phone_number),
            from_=twilio_number,
            body="Hello {0}, You are being notified by stop sound. You may be too loud".format(contact.name),
        )
    return HttpResponse(json.dumps({'message': 'sucesss'}), content_type="application/json")


@login_required
@only_superuser
def before_send_messages(request):
    return render(request, "contacts/send_messages.html")


@login_required
def get_actives(request):
    contacts = Contact.objects.filter(is_active=True)
    contacts_dict = {contact.name: str(contact.phone_number) for contact in contacts}
    return HttpResponse(json.dumps(contacts_dict), content_type="application/json")


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


@login_required
def change_actives(request):
    ids = set(map(int, request.POST['ids'].split()))
    for contact in Contact.objects.all():
        contact.is_active = contact.pk in ids
        contact.save()

    messages.success(request, 'Changed active members!')
    return HttpResponseRedirect(reverse('view_contacts'))


@login_required
def choose_settings(request):
    if request.method == "POST":
        form = ChooseASettingForm(request.POST)
        if form.is_valid():
            setting_id = int(form.cleaned_data['choice'])
            setting = Settings.objects.get(pk=setting_id)
            setting.is_active = True
            setting.save()
            messages.success(request, 'Successfully changed the sound settings')
            return HttpResponseRedirect(reverse('view_settings'))
    else:
        active_setting = Settings.objects.get(is_active=True)
        form = ChooseASettingForm(initial={'choice': active_setting.pk})

    return render(request, 'contacts/settings.html', {'form': form})

@login_required
def choose_advanced_settings(request):
    global_settings = GlobalSettings.objects.all()[0]
    if request.method == "POST":
        form = ChooseAdvanceSettingForm(request.POST)
        if form.is_valid():
            setting_choice = form.cleaned_data['choice']
            if global_settings.current_option != setting_choice or setting_choice == 'manual':
                global_settings.current_option = setting_choice
                if setting_choice == 'manual':
                    global_settings.sound_level = form.cleaned_data['sound_level']
                global_settings.current_use_count = 0
                global_settings.save()
            messages.success(request, 'Successfully changed the sound settings')
            return HttpResponseRedirect(reverse('advanced_settings'))
    else:
        curr_sound_level = global_settings.sound_level or 0
        initial = {
            'choice': global_settings.current_option,
            'sound_level': curr_sound_level
        }
        form = ChooseAdvanceSettingForm(initial=initial)

    return render(request, 'contacts/advanced_settings.html', {'form': form})
