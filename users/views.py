from .forms import UserForm
from .models import User

from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            logged_in_user = authenticate(
                username=new_user.email, 
                password=form.cleaned_data['password']
            )
            login(request, logged_in_user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserForm() 

    return render(request, 'registration/signup.html', {'form': form}) 
