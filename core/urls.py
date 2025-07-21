from django.urls import path
from core.views import client_report_pdf
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_client, name='add_client'),
    path('client/edit/<int:client_id>/', views.edit_client, name='edit_client'),
    path('client/report/', views.client_report, name='client_report'),
    path('client/report/pdf/', client_report_pdf, name='client_report_pdf'),

]
