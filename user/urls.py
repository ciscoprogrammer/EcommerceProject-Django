from django.urls import path
from . import views
from .views import (
    ProfileListCreateView,
    ProfileRetrieveUpdateDestroyView,
    AddressListCreateView,
    AddressRetrieveUpdateDestroyView,
    update_revenue
)

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('addresses/', views.AddressListView.as_view(), name='address-list'),
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyView.as_view(), name='profile-detail'),
    path('addresses/', AddressListCreateView.as_view(), name='address-list-create'),
    path('addresses/<int:pk>/', AddressRetrieveUpdateDestroyView.as_view(), name='address-detail'),
    path('users/<int:user_id>/update_revenue/', update_revenue, name='update-revenue'),

]
