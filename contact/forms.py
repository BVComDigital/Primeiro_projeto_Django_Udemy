from django import forms # Importa formularios do Django
from django.core.exceptions import ValidationError
from . import  models


# Cria o formulario de contatos
class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':  'classe-a',
                'placeholder': 'Escreva aqui',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda par ao usuário'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self. fields['first_name'].widget.attrs.update(
        #     { 
        #        'class':  'classe-a',
        #        'placeholder': 'Escreva aqui', 
        #     }
        # )


    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            )
        
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs = {
        #             'class':  'classe-a',
        #             'placeholder': 'Escreva aqui',
        #         }
        #     )
        # }
        
    
    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )
        return super().clean()
