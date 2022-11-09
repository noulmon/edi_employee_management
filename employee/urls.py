from django.urls import path

from employee import views

urlpatterns = [
    path('api/employees/', views.EmployeeList.as_view(), name='employee-list-create'),
    path('api/employee/<int:pk>/', views.EmployeeDetail.as_view(), name='employee-retrieve-update-delete'),

]
