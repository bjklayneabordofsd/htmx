from django.shortcuts import render
from core.models import Post

def posts(request):
    if request.method == 'POST':
        post = Post.objects.create(title="This is a new post")
        total = Post.objects.count()
        context = {'post': post, 'total': total}
        return render(request, 'responses/post_add.html', context)