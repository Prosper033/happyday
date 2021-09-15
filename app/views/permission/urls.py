from django.urls import path
from app.views.permission import view

urlpatterns = [
    path('create', view.create_permission, name='create_permission'),
    path('list', view.list_permission, name='list_permission'),
    path('assign_to_user/', view.assign_permission_to_user, name='assign_to_user'),
    path('assign_to_role/', view.assign_permissions_to_role, name='assign_to_role')
]
