from django.urls import path

from employee import views

urlpatterns = [
    path('api/employees/', views.EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('api/employee/<int:pk>/', views.EmployeeRetrieveUpdateDeleteView.as_view(), name='employee-retrieve-update-delete'),

]
