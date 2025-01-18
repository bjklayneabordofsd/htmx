from django.http import HttpResponse
from core.models import Post

def posts(request):
    if request.method == 'POST':
        post = Post.objects.create(title="This is a new post")
        return HttpResponse(f"This is you new post {post.title}")