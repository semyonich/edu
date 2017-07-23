from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout

from accounts.forms import LoginForm

def sign_in(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('all_articles'))
    else:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(email=data.get('email'), password=data.get('password'))
                if user:
                    login(request, user)
                    return HttpResponseRedirect(reverse('all_articles'))
                else:
                    print('Invalid User!')

        return render(request, 'sign_in.html', {'form': form})

def sign_out(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect(reverse('sign_in'))
    else:
        return HttpResponseRedirect(reverse('all_articles'))
