from sale_management.models import Employee
from django.views import generic

class DetailView(generic.DetailView):
    template_name = 'employee/detail.html'
    model = Employee


class ListView(generic.ListView):
    template_name = 'employee/list.html'
    context_object_name = 'latest_employee_list'

    def get_queryset(self):
        return Employee.objects.order_by('-created_at')
    
