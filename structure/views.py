from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View

from structure.forms import UserLoginForm
from structure.models import Position, Employee
from django.contrib.auth.views import (LoginView, PasswordChangeView,
                                       PasswordResetConfirmView,
                                       PasswordResetView)
# Create your views here.


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'structure/index.html'

    # def get_success_url(self):
    #     return reverse_lazy('structure:structure_company')


class StructureCompanyTemplateView(TemplateView):
    template_name = 'structure/structure-company.html'


class PositionView(View):
    def get(self, request, position_id):
        position = Position.objects.filter(id=position_id).first()

        context = {
            'position_name': position.name,
        }
        return render(request, 'structure/position-view.html', context=context)
