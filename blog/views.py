from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from .models import Post

def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    posts = Post.objects.order_by('created_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})
