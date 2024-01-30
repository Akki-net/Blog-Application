from django.shortcuts import render, get_object_or_404
from .model import Post
from django.http import Http404

def post_list(request):
    posts = Post.published.all()
    return render(request, 
                'blog/post/list.xhtml',
                {'posts': posts})

def post_detail(request, id):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404('No Post found.')

    # alternative way
    post = get_object_or_404(Post,  
                        id=id, 
                        status=Post.Status.PUBLISHED)
    return render(request,
                'blog/post/detail.xhtml',
                {'post': post})