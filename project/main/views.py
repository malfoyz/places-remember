from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render


def index(request: HttpRequest) -> HttpResponse:
    """Home page handler"""

    return render(
        request=request,
        template_name='main/index.html',
        # context=context,
    )


def add_memory(request: HttpRequest) -> HttpResponse:
    """Memory add page handler"""

    pass


def logout_view(request: HttpRequest) -> HttpResponseRedirect:
    """Exit handler"""

    logout(request)
    return redirect('main:index')
