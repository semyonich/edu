from django.conf.urls import url

from blog.views import blogs, single_blog, user_articles

urlpatterns = [
    url(r'^$', blogs, name='all_articles'),
    url(r'^single/(?P<article_id>[0-9]+)$', single_blog, name='single_article_page'),
    url(r'^user/(?P<user_id>\d+)/$', user_articles, name='user_articles'),
]