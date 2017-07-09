from django.shortcuts import render, get_object_or_404

from blog.models import Article

# Create your views here.
def blogs(request):
    keyword = request.POST.get('keyword', '')
    articles = Article.objects.filter(title__contains=keyword)
    return render(request, 'blogs.html', {'articles': articles})


def single_blog(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'single_blog.html', {'article': article})

