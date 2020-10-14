from django.urls import path
from . import views

urlpatterns = [
    path('faq/', views.faq, name='faq'),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('publications/', views.publications, name='publications'),
    path('upload_all/', views.upload_all, name='upload'),
]
