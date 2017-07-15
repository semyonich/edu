from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User

from blog.models import Article

from utils import gen_page_list

# Create your views here.
def blogs(request):
    # keyword = request.POST.get('keyword', '')
    page = request.GET.get('page', 1)
    p = Paginator(Article.objects.all(), 2)
    # filter(title__contains=keyword)
    try:
        final_articles = p.page(page)
    except PageNotAnInteger:
        final_articles = p.page(1)
    except EmptyPage:
        final_articles = p.page(p.num_pages)
    return render(request, 'blogs.html', {'articles': final_articles,
                                          'pagination': gen_page_list(page, p.num_pages)})


def single_blog(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'single_blog.html', {'article': article})

def user_articles(request, user_id):
    user = get_object_or_404(User, id=user_id)
    articles = Article.objects.filter(author=user)
    return render(request, 'user_blog.html', {'articles': articles,
                                              'user': user})


