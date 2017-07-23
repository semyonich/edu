from django.conf.urls import url

from blog.views import blogs, single_blog, user_articles, like_article

urlpatterns = [
    url(r'^$', blogs, name='all_articles'),
    url(r'^single/(?P<article_id>\d+)/$', single_blog, name='single_article_page'),
    url(r'^single/(?P<article_id>\d+)/like/$', like_article, name='like_article'),
    url(r'^user/(?P<user_id>\d+)/$', user_articles, name='user_articles'),
]