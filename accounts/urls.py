from django.conf.urls import url

from accounts.views import sign_in, sign_out, get_user_rest

urlpatterns = [
url(r'^sign-in/$', sign_in, name='sign_in'),
url(r'^sign-out/$', sign_out, name='sign_out'),
url(r'^get-user-rest/$', get_user_rest, name='get_user_rest'),
]