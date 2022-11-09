from django.urls import path

from employee import views

urlpatterns = [
    path('api/employees/', views.EmployeeList.as_view()),
    path('api/employee/<int:pk>/', views.EmployeeDetail.as_view()),

]
