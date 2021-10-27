from django.contrib import admin
from .models import Receita

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'publicada')
    # posso colocar quantos atributos eu quiser do modelo Receitas, como 'tempo_preparo', 'rendimento', etc.
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria', )
    list_editable = ('publicada',)
    list_per_page = 5

admin.site.register(Receita, ListandoReceitas)
# registra o modelo (classe Receitas) e o display da classe Listando receita
