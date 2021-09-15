from django.shortcuts import render, redirect
from app.dto.role_dto import *
from app.service_provider import auth_service_provider
from app.utiles.decorators import login_required


@login_required
def create_role(request):
    context = {

    }
    __create_role(request, context)
    if context is not {}:
        return render(request, 'Role/createrole.html', context)
    return render(request, 'Role/createrole.html', context)


@login_required
def assign_role(request):
    user = auth_service_provider.user_management_service().get_all_for_select_list()
    role = auth_service_provider.role_management_service().get_all_for_select_list()
    context = {
        'user': user,
        'role': role

    }
    __create_assignment(request, context)
    if context is not {}:
        return render(request, 'Role/assignrole.html', context)
    return render(request, 'Role/assignrole.html', context)


@login_required
def list_role(request):
    roles = auth_service_provider.role_management_service().list()
    context = {
        'roles': roles
    }
    return render(request, 'Role/listrole.html', context)


@login_required
def edit_role(request, role_id: int):
    role: GetRoleDto = auth_service_provider.role_management_service().get(role_id=role_id)
    context = {
        'role': role
    }
    __edit_if_post_method(request, context, role_id)
    if request.method == 'POST':
        return redirect("list_role")
    return render(request, 'Role/editrole.html', context)


@login_required
def get_role(request, role_id: int):
    role = auth_service_provider.role_management_service().get(role_id=role_id)
    if role:
        context = {
            'role': role
        }
    else:
        context = {
            'message': 'user not fount'
        }
    return render(request, 'Role/editrole.html', context)


def __edit_if_post_method(request, context: dict, role_id: int):
    if request.method == 'POST':
        role = __get_attribute_form_request_edit(request)
        result = auth_service_provider.role_management_service().edit(role_id=role_id, model=role)
        context['saved'] = result


def __get_attribute_form_request_edit(request):
    edit_role_dto = EditRoleDto()
    edit_role_dto.name = request.POST['name']
    edit_role_dto.description = request.POST['description']
    return edit_role_dto


def __create_assignment(request, context):
    if request.method == "POST":
        assignment = __get_role_and_user(request)
        result = auth_service_provider.role_management_service().assign(assignment)
        context['saved'] = result


def __get_role_and_user(request):
    assignment_dto = AssignRoleToUserDto()
    assignment_dto.role_id = request.POST['role_id']
    assignment_dto.user_id = request.POST['user_id']
    return assignment_dto


def __create_role(request, context):
    if request.method == 'POST':
        role = __get_attribute_from_request(request)
        result = auth_service_provider.role_management_service().create(role)
        context['saved'] = result


def __get_attribute_from_request(request):
    role_dto = CreateRoleDto()
    role_dto.name = request.POST['name']
    role_dto.description = request.POST['description']
    return role_dto
