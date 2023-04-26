from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .models import PlaceMemory


def index(request: HttpRequest) -> HttpResponse:
    """Home page handler"""

    memories = PlaceMemory.objects.filter(user=request.user.pk)
    context = {
        'memories': memories,
    }

    return render(
        request=request,
        template_name='main/index.html',
        context=context,
    )


def add_memory(request: HttpRequest) -> HttpResponse:
    """Memory add page handler"""

    pass


def logout_view(request: HttpRequest) -> HttpResponseRedirect:
    """Exit handler"""

    logout(request)
    return redirect('main:index')
