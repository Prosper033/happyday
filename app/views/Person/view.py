import json
from django.http import HttpRequest
from app.service_provider import auth_service_provider
from app.dto.user_dto import *
from django.shortcuts import redirect, render
from app.utiles.decorators import login_required
from app.utiles.utility import hash_value


def create_user(request):
    context = {

    }
    __create_if_post_method(request, context)
    if context is not {}:
        return render(request, 'user/create.html', context)
    return render(request, 'user/create.html', context)


@login_required
def edit_user(request, user_id: int):
    user: UserDetailsDto = auth_service_provider.user_management_service().get_user(user_id=user_id)
    context = {
        'user': user
    }
    __edit_if_post_method(request, context, user_id)
    if request.method == 'POST':
        return redirect("list_user")
    return render(request, 'user/Edit.html', context)


def login_get(request):
    next_url = request.session.get("next", '/')
    try:
        request.session.__delitem__("next")
    except KeyError:
        ...
    context = {
        'next': next_url

    }
    return render(request, 'user/login.html', context)


@login_required
def list_user(request):
    users = auth_service_provider.user_management_service().list_user()
    context = {
        'users': users
    }

    return render(request, 'user/List.html', context)


def login_post(request):
    context = {}
    user = LoginUserDto()
    redirect_field = request.GET['next']
    user.email = request.POST['email']
    user.password = request.POST['password']
    authenticated_user = authenticate(email=user.email, password=user.password)
    if authenticated_user:
        login(authenticated_user, request)
        return redirect(redirect_field)
    else:
        context['message'] = "email or password incorrect"
        context['next'] = redirect_field
        return render(request, 'user/login.html', context)


def authenticate(email: str, password: str):
    user = Authenticate()
    user.password = hash_value(password)
    user.email = email
    user = auth_service_provider.user_management_service().authenticate(user)
    if user:
        return user


def login(user: UserDetailsDto, request: HttpRequest):
    user_data = json.dumps(user.__dict__)
    request.session.__setitem__("user", user_data)


def logout(request: HttpRequest):
    try:
        request.session.__delitem__("user")
    except KeyError:
        ...
    return redirect('home')


@login_required
def get_user(request, user_id: int):
    user = auth_service_provider.user_management_service().get_user(user_id=user_id)
    if user:
        context = {
            'user': user
        }
    else:
        context = {
            'message': 'user not fount'
        }
    return render(request, 'user/Details.html', context)


def __get_attribute_form_request_edit(request):
    edit_user_dto = EditUserDto()
    edit_user_dto.email = request.POST['email']
    edit_user_dto.last_name = request.POST['last_name']
    edit_user_dto.first_name = request.POST['first_name']
    edit_user_dto.phone_number = request.POST['phone_number']
    return edit_user_dto


def __get_attribute_from_request_create(request):
    create_user_dto = CreateUserDto()
    create_user_dto.email = request.POST['email']
    create_user_dto.phone_number = request.POST['phone_number']
    create_user_dto.last_name = request.POST['last_name']
    create_user_dto.first_name = request.POST['first_name']
    create_user_dto.password = request.POST['password']
    create_user_dto.confirm_password = request.POST['confirm_password']
    return create_user_dto


def __create_if_post_method(request, context: dict):
    if request.method == 'POST':
        user = __get_attribute_from_request_create(request)
        if user.password == user.confirm_password:
            user.password = hash_value(user.password)
            result = auth_service_provider.user_management_service().create_user(user)
            context['saved'] = result
        else:
            context['message'] = "Password dose not match"


def __edit_if_post_method(request, context: dict, user_id: int):
    if request.method == 'POST':
        user = __get_attribute_form_request_edit(request)
        result = auth_service_provider.user_management_service().edit_user(user_id=user_id, model=user)
        context['saved'] = result
