from django.shortcuts import render, redirect
from django.contrib import messages
from contact.forms import RegisterForm

def register(request):
    form = RegisterForm()

    # messages.info(request, 'Bem vindo ao sistema de registro.')
    # messages.success(request, 'Sucesso no registro.')
    # messages.warning(request, 'Atenção necessária.')
    # messages.error(request, 'Erro no registro.')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sucesso no registro.')
            return redirect('contact:index')
          #  form = RegisterForm()   Reset the form after successful registration


    return render(request, 
                  'contact/register.html',
                  {
                      'form': form
                  }
                )
