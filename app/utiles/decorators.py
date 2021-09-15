from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect

REDIRECT_FIELD_NAME = 'next'
LOGIN_URL = "login_get"


def login_required(function):
    def inner(request: HttpRequest, *args, **kwargs):
        user = request.session.get("user", default=None)
        if user:
            return function(request, *args, **kwargs)
        else:
            request.session.__setitem__(REDIRECT_FIELD_NAME, request.build_absolute_uri())
            return redirect(LOGIN_URL)

    return inner


def is_authorized(function):
    ...


def has_perm(function):
    def inner(request: HttpRequest, *args, **kwargs):
        user = request.session.get("user", default=None)
        if "" in user:
            return function(request, *args, **kwargs)
        else:
            request.session.__setitem__(REDIRECT_FIELD_NAME, request.build_absolute_uri())
            return redirect(LOGIN_URL)

    return inner


def allowed_method(function):
    ...
