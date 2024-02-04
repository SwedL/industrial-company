from django.shortcuts import render
from django.views.generic import TemplateView, View

from structure.models import Position, Employee

# Create your views here.


class IndexTemplateView(TemplateView):
    template_name = 'company/index.html'
    # template_name = 'company/structure_of_company.html'


class PositionView(View):

    def get(self, request, position_id):

        position = Position.objects.filter(id=position_id).first()

        context = {
            'position_name': position.name,
        }
        return render(request, 'company/position-view.html', context=context)
