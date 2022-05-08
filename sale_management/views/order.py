from django.views import generic
from sale_management.models import Order, OrderDetail

class ListView(generic.ListView):
    template_name = 'order/list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.all


class DetailView(generic.DetailView):
    model = Order
    template_name = "order/detail.html"
