from django.views import generic
from .models import Member


class IndexView(generic.ListView):
    template_name = 'members/index.html'

    def get_queryset(self):
        return Member.objects.order_by('start_date')


