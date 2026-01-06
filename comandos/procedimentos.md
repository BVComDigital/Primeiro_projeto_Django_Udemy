Após criar um app, colocar o app no INSTALLED_APPS, do settings do projeto 
Configura a pasta base de templats e arquivos estaticos 
Colocar o caminho das pastas templates e static no settings
Templates no:
    TEMPLATES = [
    {
        .....
            BASE_DIR / 'base_templates',
        ],

Para o arquivo estaticos, cria o caminho:

    STATICFILES_DIRS = (
        BASE_DIR / 'base_static',
    )

Cria no app a pasta templates e a pasta (name_space, que tem o mesmo nome do app)
cria o arquivo indenx.html, e faz uma extends :
{% extends "global/base.html" %}

Cria no app um arquivo urls.py
    from django.urls import path
    from contact import views

    app_name = 'contact'

    urlpatterns = [
        path('', views.index, name='index'),
    ]

Passa a url criada em contacts para a url do projeto:
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('', include('contact.urls')),
        path('admin/', admin.site.urls),
    ]

Alterar o projeto e mandar para o servidor via Git

    Aletra o projeto onde for necessário
    faz um $ git add .
    faz um $ git commit -m 'mensagem'
    faz um $ git remote -v -> para verificar servidor
    faz um $ git push origin main -> manda para o GitHub
    faz um $ git push agendarepo main -> manda para o repositorio (agendarepo)
    Vai no servidor, entra no agendaapp
    faz um $ git pull agendarepo main -> trouxe os commit dos projetos
    Atualiza o gunicorn para ele pegar os novos arquivos
    faz um $ sudo systemctl restart agenda
    Se precisar faz um restart no nginx
    faz um $ sudo systemctl restart agenda



Criar um superusuario para acessar área administrativa do django

Usuário: Bruno
email : bruno@bv.com
senha: XgtwkHj@TCPf8jH  

Usuário: Bruno
email : bruno2@bv.com
senha: 4aAcUpg57hWf@4S