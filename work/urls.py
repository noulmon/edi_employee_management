from django.urls import path

from work import views

urlpatterns = [
    path('api/work_arrangements/', views.WorkArrangementListCreateView.as_view(), name='work-arrangement-list-create'),
    path('api/work_arrangements/<int:pk>/', views.WorkArrangementRetrieveUpdateDeleteView.as_view(),
         name='work-arrangement-retrieve-update-delete'),
]
