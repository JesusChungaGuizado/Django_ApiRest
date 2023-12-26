from django.urls import path
from ..adapters.django.views import user_view



urlpatterns = [
    path('users',user_view.UserViewSet.as_view({'get':'list','post': 'create'}),name='getUsers'),
    path('user/<int:id>', user_view.UserViewSet.as_view({'get': 'show', 'put': 'update','delete': 'destroy'}), name='getUserById'),

]