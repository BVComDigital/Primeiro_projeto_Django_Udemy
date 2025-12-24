from django.shortcuts import render
from contact.forms import RegisterForm

def register(request):
    form = RegisterForm

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form = RegisterForm()  # Reset the form after successful registration


    return render(request, 
                  'contact/register.html',
                  {
                      'form': form
                  }
                )
    """Cadastro de /Usuários"""
    # form = RegisterForm(request.POST or None)

    # if form.is_valid():
    #     user = form.save(commit=False)
    #     user.set_password(user.password)
    #     user.save()
    #     messages.success(request, 'Usuário cadastrado com sucesso')
    #     return redirect('contact:register')

    # context = {
    #     'form': form,
    #     'form_action': reverse('contact:register'),
    # }

    # return render(request, 'contact/register.html', context)
