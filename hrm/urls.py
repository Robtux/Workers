from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index-hrm'),
    path('employees/', views.EmployeeListView.as_view(), name='employees'),
    path('employees/<int:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),
]