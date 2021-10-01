from django.urls import path
from crud_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('save-data/', views.save_data, name='save_data'),
    path('delete-data/', views.delete_data, name='delete_data'),
    path('edit-data/', views.edit_data, name='edit_data'),

]
