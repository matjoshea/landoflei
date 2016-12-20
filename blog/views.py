from django.views import generic
from .models import Post


class IndexView(generic.ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Post.objects.order_by('-published_date')[:8]

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
