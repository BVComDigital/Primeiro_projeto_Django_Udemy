from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q # Para colocar o ou nos filtros de busca
from contact.models import Contact

def index(request):

    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')[10:20] # Seleciona os contatos e ordena por id decrescente.

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def search(request):
    search_value = request.GET.get('q', '').strip()
#    Pega o valor q do imput(name='q') do _header
    print('search_value', search_value)

    if search_value == '':
        return redirect('contact:index')
    # Checa se o valor foi enviado, se não retorna para o index



    contacts = Contact.objects\
        .filter(show=True)\
        .filter(
                Q(first_name__icontains=search_value) |
                Q(last_name__icontains=search_value) |
                Q(email__icontains=search_value) |
                Q(phone__icontains=search_value),
            )\
        .order_by('-id') # Seleciona os contatos e ordena por id decrescente. Filtra usando a função Q que permite o 'OU'. Pode colocar uma busca do google dentro do Django
    
    print(contacts.query) # debuga a busca

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - ',
        'search_value': search_value,
    }

    return render(
        request,
        'contact/index.html',
        context
    )


    
def contact(request, contact_id):
    # single_contact = Contact.objects.filter(id=contact_id).first()
    single_contact = get_object_or_404(Contact, id=contact_id, show=True)
    # Coloca show True para esconder os contatos que não estão a vista no admin 

    site_title = f'{single_contact.first_name} {single_contact.last_name}'
    
    context = {
        'contact': single_contact,
        'site_title': site_title
    }

    return render(
        request,
        'contact/contact.html',
        context
    )
