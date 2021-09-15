from app.service_provider import auth_service_provider
from app.dto.permission_dto import *
from django.shortcuts import render
from app.utiles.decorators import login_required


@login_required
def create_permission(request):
    context = {
        'saved': ''

    }
    __create_if_post(request, context)
    if context['saved']:
        return render(request, "permission/create_permission.html", context)
    return render(request, "permission/create_permission.html", context)


@login_required
def assign_permissions_to_role(request):
    permissions = auth_service_provider.permission_management_service().list_permission()
    roles = auth_service_provider.role_management_service().list()
    permission = auth_service_provider.permission_management_service().get_all_for_select_list()
    role = auth_service_provider.role_management_service().get_all_for_select_list()
    context = {
        'permissions': permissions,
        'roles': roles,
        'saved': '',
        'permission': permission,
        'role': role
    }
    __create_assignment(request, context)
    if context['saved']:
        return render(request, 'permission/assign_permission_to_role.html', context)
    return render(request, 'permission/assign_permission_to_role.html', context)


@login_required
def assign_permission_to_user(request):
    permissions = auth_service_provider.permission_management_service().list_permission()
    users = auth_service_provider.user_management_service().list_user()
    permission = auth_service_provider.permission_management_service().get_all_for_select_list()
    user = auth_service_provider.user_management_service().get_all_for_select_list()
    context = {
        'permissions': permissions,
        'users': users,
        'saved': '',
        'user': user,
        'permission': permission
    }
    __create_assignment(request, context)
    if context['saved']:
        return render(request, 'permission/assign_permission_to_user.html', context)
    return render(request, 'permission/assign_permission_to_user.html', context)


@login_required
def list_permission(request):
    permission = auth_service_provider.permission_management_service().list_permission()
    context = {
        'permission': permission,
        'saved': ''
    }
    return render(request, 'permission/list_permission.html', context)


def list_permission_assignment():
    permissions = auth_service_provider.permission_management_service().list_permission()
    permissions_list = []
    for permission in permissions:
        permissions_list.append(int(permission.id))
    return permissions_list


def list_role_assignment():
    roles = auth_service_provider.role_management_service().list()
    role_list = []
    for role in roles:
        role_list.append(int(role.id))
    return role_list


def list_user_assignment():
    users = auth_service_provider.user_management_service().list_user()
    user_list = []
    for user in users:
        user_list.append(int(user.id))
    return user_list


def __get_attribute_from_request(request):
    permission_dto = CreatePermissionDto()
    permission_dto.name = request.POST['name']
    permission_dto.description = request.POST['description']
    return permission_dto


def __create_if_post(request, context):
    if request.method == "POST":
        permission = __get_attribute_from_request(request)
        result: bool = auth_service_provider.permission_management_service().create_permission(permission)
        context['saved'] = result


def __get_role_and_perm_from_request(request):
    assignment_dto = AssignPermissionToRoleDto()
    assignment_dto.role_id = request.POST.get('role_id', None)
    assignment_dto.permission_id = request.POST.get('permission_id', None)
    return assignment_dto


def __get_user_and_perm_from_request(request):
    assignment_dto = AssignPermissionToUserDto()
    assignment_dto.user_id = request.POST.get('user_id', None)
    assignment_dto.permission_id = request.POST.get('permission_id', None)
    return assignment_dto


def __create_assignment(request, context):
    if request.method == 'POST':
        assignment = __get_role_and_perm_from_request(request)
        if assignment.role_id is not None:
            result = auth_service_provider.permission_management_service().assign_to_user(assignment)
            context['saved'] = result
        else:
            assignment = __get_user_and_perm_from_request(request)
            result = auth_service_provider.permission_management_service().assign_to_user(assignment)
            context['saved'] = result
