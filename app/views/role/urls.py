from django.urls import path
from app.views.role import view

urlpatterns = [
    path('create', view.create_role, name='create_role'),
    path('list', view.list_role, name='list_role'),
    path('assign_role', view.assign_role, name='assign_role'),
    path("edit/<int:role_id>", view.edit_role, name="edit_role"),
    path("role_details/<int:role_id>", view.get_role, name='get_role')

]
