from django.views import generic
from sale_management.models import Product

class DetailView(generic.DetailView):
    model = Product
    template_name = 'product/detail.html'


class ListView(generic.ListView):
    template_name = 'product/list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all
    