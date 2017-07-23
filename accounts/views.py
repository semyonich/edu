from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.forms import LoginForm
from accounts.models import User
from accounts.serializers import UserSerializer, UserCreationSerializer

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

@api_view(['GET', 'POST'])
def get_user_rest(request):
    if request.method == 'GET':
        # serializer for return formatted data
        user = User.objects.get(pk=2)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserCreationSerializer(data=request.POST)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            print(validated_data)
            return Response({'success': True})
        else:
            return Response(serializer.errors)



