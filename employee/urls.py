from django.urls import path

from employee import views

urlpatterns = [
    # Employee URLs
    path('api/employees/', views.EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('api/employee/<int:pk>/', views.EmployeeRetrieveUpdateDeleteView.as_view(),
         name='employee-retrieve-update-delete'),

    # Team URLs
    path('api/teams/', views.TeamListCreateView.as_view(), name='team-list-create'),
    path('api/team/<int:pk>/', views.TeamRetrieveUpdateDeleteView.as_view(), name='team-retrieve-update-delete'),

    # Team leader URLs
    path('api/team_leaders/', views.TeamLeaderListCreateView.as_view(), name='teamleader-list-create'),
    path('api/team_leader/<int:pk>/', views.TeamLeaderRetrieveUpdateDeleteView.as_view(),
         name='teamleader-retrieve-update-delete'),
    # Employee monthly payment end point
    path('api/payment_list/', views.EmployeeMonthlyPaymentList.as_view(), name='employee-monthly-payment'),

]
