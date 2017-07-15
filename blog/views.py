from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from blog.models import Article

# Create your views here.
def blogs(request):
    keyword = request.POST.get('keyword', '')
    articles = Article.objects.filter(title__contains=keyword)
    return render(request, 'blogs.html', {'articles': articles})


def single_blog(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'single_blog.html', {'article': article})

def user_articles(request, user_id):
    user = get_object_or_404(User, id=user_id)
    articles = Article.objects.filter(author=user)
    return render(request, 'user_blog.html', {'articles': articles,
                                              'user': user})


