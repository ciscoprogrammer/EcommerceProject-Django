from django.urls import path
from . import views


urlpatterns = [
    path('orders/', views.OrderListView.as_view(), name='order-list'),
     path('metrics/', views.order_metrics, name='order-metrics'),
]
