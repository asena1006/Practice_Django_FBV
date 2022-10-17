from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import Post

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
        #instagram/templates/instagram/post_list.html
    return render(request, 'instagram/post_list.html',{
        'post_list': qs,
        'q': q,
    })

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html',{
#         'post': post,
#     })
post_detail = DetailView.as_view(model=Post)