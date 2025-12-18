from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = '-id', #se colocar - na frente ordena decrescente
    #list_filter = 'created_date', -> pesquisa pela data de criação
    search_fields = 'id', 'first_name', 'last_name', #camps de pesquisa
    list_per_page = 10 #qts exibe na página
    list_max_show_all = 200 #max exibido na pagina, se não limitar ele mostra tudo
    list_editable = 'first_name', 'last_name', #para editar campos
    list_display_links = 'id', 'phone', #cria um link nestes campos
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name', 
    ordering = '-id',
