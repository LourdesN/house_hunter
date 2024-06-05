from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form.html', views.form_view, name='form_html'), 
    path('form/', views.form_view, name='form'),
    path('apartments/', views.apartment_list, name='apartment_list'),
    path('list.html', views.apartment_list, name='apartment_list'),
]
