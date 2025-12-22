from django.urls import path
from . import views

urlpatterns = [
    path('submit', views.submit, name='submit'),
    path('detail', views.detail, name='detail'),
    path('test-panel/', views.test_panel, name='test_panel'),
]
