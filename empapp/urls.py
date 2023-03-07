from django.urls import path,include
from empapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('handlelogout',views.handlelogout,name='handlelogout'),
    path('employees',views.employees,name='employees'),
    path('update_employees/<int:empid>',views.update_employees,name='update_employees'),
    path('delete_employees/<int:empid>',views.delete_employees,name='delete_employees'),
    path('department',views.department,name='department'),
    path('update_department/<int:departid>',views.update_department,name='update_department'),
    path('delete_department/<int:departid>',views.delete_department,name='delete_department'),
    path('client',views.client,name='client'),
    path('delete_client/<int:clientid>',views.delete_client,name='delete_client'),
    path('update_client/<int:clientid>',views.update_client,name='update_client'),
    
]