from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients, name='clients'),
    path('clients/about/', views.about, name='about'),
    path('clients/service1/', views.service1, name='service1'),
    path('clients/service2/', views.service2, name='service2'),
    path('clients/service3/', views.service3, name='service3'),
    path('clients/contact/', views.contact, name='contact'),
    path('clients/request-service/', views.request_service, name='request_service'),
    path("clients/admin_login/", views.admin_login, name="admin_login"),
    path("clients/admin_signup/", views.admin_signup, name="admin_signup"),

]   