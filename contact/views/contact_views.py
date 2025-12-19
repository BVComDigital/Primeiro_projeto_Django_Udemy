from django.shortcuts import render, get_list_or_404
from contact.models import Contact
from django.http import Http404

def index(request):

    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')[:10] # Seleciona os contatos e ordena por id decrescente.

    context = {
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context
    )
    
def contact(request, contact_id):
    # single_contact = Contact.objects.filter(id=contact_id).first()
    single_contact = get_list_or_404(Contact.objects, pk=contact_id, show=True)
    # Coloca show True para esconder os contatos que não estão a vista no admin 
    if single_contact is None:
        raise Http404

    context = {
        'contact': single_contact,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )
