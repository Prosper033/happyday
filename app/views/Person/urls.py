from django.urls import path
from app.views.user import view

urlpatterns = [
    path('', view.logout, name='logout'),
    path('create', view.create_user, name="create_user"),
    path('login/', view.login_get, name="login_get"),
    path("login_post", view.login_post, name="login_post"),
    path("edit/<int:user_id>", view.edit_user, name="edit_user"),
    path('list', view.list_user, name="list_user"),
    path("user_details/<int:user_id>", view.get_user, name='get_user')

]
