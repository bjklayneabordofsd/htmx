from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    total = Post.objects.count()
    context = {'posts':posts, 'total':total}
    return render(request, 'index.html', context)
