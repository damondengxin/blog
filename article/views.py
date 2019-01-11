from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Post


def post_list(request):
    posts = Post.published.all()
    # paginator = Paginator(object_list,2)
    # page = request.GET.get('page')
    # try:
    #     posts = paginator.page(page)
    # except PageNotAnInteger:
    #     posts = paginator.page(1)
    # except EmptyPage:
    #     posts = paginator.page(paginator.num_pages)
    return render(request, 'article/list.html',locals())

def post_detail(request,year, month, day, post):
    print(Post)
    post = get_object_or_404(Post,slug=post, status='published',publish__year=year, publish__month=month,
                             publish__day=day)

    return render(request, 'article/detail.html',locals())