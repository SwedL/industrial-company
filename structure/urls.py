"""Определяет схемы URL для carwash"""

from django.urls import path

from .views import *

app_name = 'structure'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='home'),
    path('position/<int:position_id>/', PositionView.as_view(), name='position_view'),
    # path('request-call/', RequestCallFormView.as_view(), name='call_me'),
    # path(
    #     'request-call-processing/<int:days_delta>/<int:call_pk>/',
    #     RequestCallProcessingView.as_view(),
    #     name='request_call_processing',
    # ),
    # path('staff/<int:days_delta>/', StaffDetailView.as_view(), name='staff'),
    # path('cancel/<int:days_delta>/<int:registration_id>/', StaffCancelRegistrationView.as_view(), name='cancel'),
    # path('user-registrations/', UserRegistrationsListView.as_view(), name='user_registrations'),
    # path('user-reg-cancel/<int:registration_pk>/', UserRegistrationsCancelView.as_view(), name='user_reg_cancel'),
]
