__author__ = 'cosme.cardoso'
#coding:utf-8

from django.contrib import admin

from models import Pessoa
from models import Lugar
from models import TipoAcesso
from models import Permissao

class PessoaAdmin(admin.ModelAdmin):

	list_display = ['Nome','Cartao','CPF']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True

class LugarAdmin(admin.ModelAdmin):

	 list_display = ['NomeLugar']
	 list_filter = ['NomeLugar']
	 search_fields = ['NomeLugar']

class TipoAcessoAdmin(admin.ModelAdmin):
	 list_display = ['Nivel']
	 list_filter = []
	 search_fields = ['Nivel']

class PermissaoAdmin(admin.ModelAdmin):
	 list_display = ['Pessoa','Lugar','TipoAcesso','Permissao']
	 list_filter = []
	 search_fields = ['Pessoa','Lugar','TipoAcesso','Permissao']

admin.site.register(Pessoa,PessoaAdmin)
admin.site.register(Lugar, LugarAdmin)
admin.site.register(TipoAcesso,TipoAcessoAdmin)
admin.site.register(Permissao,PermissaoAdmin)
