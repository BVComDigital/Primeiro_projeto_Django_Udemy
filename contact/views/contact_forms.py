from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q # Para colocar o ou nos filtros de busca
from django.core.paginator import Paginator
from contact.models import Contact

def create(request):


    context = {
    }

    return render(
        request,
        'contact/create.html',
        context
    )
