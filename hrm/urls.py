from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index-hrm'),
    path('workers/', views.WorkerListView.as_view(), name='workers'),
    path('workers/<int:pk>', views.WorkerDetailView.as_view(), name='worker-detail'),
]