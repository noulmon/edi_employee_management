from django.urls import path

from work import views

urlpatterns = [
    path('api/work_arrangements/', views.WorkArrangementListCreateView.as_view(), name='work-arrangement-list-create'),
    path('api/work_arrangements/<int:pk>/', views.WorkArrangementRetrieveUpdateDeleteView.as_view(),
         name='work-arrangement-retrieve-update-delete'),

    path('api/employee_work_arrangements/', views.EmployeeWorkArrangementListCreateView.as_view(),
         name='employee-work-arrangement-list-create'),
    path('api/employee_work_arrangements/<int:pk>/', views.EmployeeWorkArrangementRetrieveUpdateDeleteView.as_view(),
         name='employee-work-arrangement-retrieve-update-delete'),
]
