from django.shortcuts import render, redirect
from django.contrib import messages, auth
from contact.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm


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
            messages.success(request, 'Registro realizado com sucesso!')
            return redirect('contact:login')
          #  form = RegisterForm()   Reset the form after successful registration


    return render(request, 
                  'contact/register.html',
                  {
                      'form': form
                  }
                )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Login realizado com sucesso.')
            return redirect('contact:index')
        messages.error(request, 'Erro no login. Verifique seus dados.')

    return render(request, 
                  'contact/login.html',
                  {
                      'form': form
                  }
                )

def logout_view(request):
    auth.logout(request)
    messages.info(request, 'Logout realizado com sucesso.')
    return redirect('contact:login')