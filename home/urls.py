from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='indeex'),
    path('form/', views.form, name='form'),
    path('submit/', views.submit, name='submit'),
    path('result/<int:developer_id>', views.result, name='result'),
    path('all_results/', views.all_results, name='all_results'),

]
