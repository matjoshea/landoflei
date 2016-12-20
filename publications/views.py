from django.views import generic
from .models import Publication


class IndexView(generic.ListView):
    template_name = 'publications/index.html'

    def get_queryset(self):
        return Publication.objects.order_by('-pub_date')

