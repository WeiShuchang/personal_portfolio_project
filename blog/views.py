from django.shortcuts import render, get_object_or_404
from .models import Blogs

# Create your views here.
def blogs(request):
    blogs = Blogs.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blog/detail.html', {'id':blog_id, 'blog':blog})