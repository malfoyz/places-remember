from typing import Union

from django.contrib.auth import logout
from django.http import (HttpRequest, HttpResponse, HttpResponseForbidden,
                         HttpResponseRedirect)
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PlaceMemoryForm
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


def add_memory(request: HttpRequest) -> Union[HttpResponse, HttpResponseRedirect]:
    """Memory add page handler"""

    context = {'title': 'Adding a memory'}

    if request.method == 'POST':
        pm_form = PlaceMemoryForm(request.POST)
        if pm_form.is_valid():
            pm_form.save()
            return redirect('main:index')
        else:
            context['form'] = pm_form
            return render(request, 'main/add_memory.html', context)
    else:
        pm_form = PlaceMemoryForm(initial={'user': request.user.pk})
        context['form'] = pm_form
        return render(request, 'main/add_memory.html', context)
    

def edit_memory(request: HttpRequest, pk: int) -> Union[HttpResponse, HttpResponseRedirect]:
    """Memory edit page handler"""

    memory = get_object_or_404(PlaceMemory, pk=pk)
    if memory.user.pk == request.user.pk:
        context = {'title': 'Memory change'}

        if request.method == 'POST':
            pm_form = PlaceMemoryForm(request.POST, instance=memory)
            if pm_form.is_valid():
                pm_form.save()
                return redirect('main:index')
            else:
                context['form'] = pm_form
                return render(request, 'main/add_memory.html', context)
        else:
            pm_form = PlaceMemoryForm(instance=memory)
            context['form'] = pm_form
            return render(request, 'main/add_memory.html', context)
    else:
        return HttpResponseForbidden('You are not allowed to edit someone else\'s post!')


def delete_memory(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    """Memory delete handler"""

    memory = get_object_or_404(PlaceMemory, pk=pk)
    if memory.user.pk == request.user.pk:
        if request.method == 'POST':
            memory.delete()
            return redirect('main:index')
        else:
            context = {'place': memory.place}
            return render(
                request=request, 
                template_name='main/confirm_deletion.html',
                context=context,
            )
    else:
        return HttpResponseForbidden('You are not allowed to delete someone else\'s post!')


def logout_view(request: HttpRequest) -> HttpResponseRedirect:
    """Exit handler"""

    logout(request)
    return redirect('main:index')
