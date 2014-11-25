__author__ = 'cosme.cardoso'
# coding:utf-8
from django.db import models
from django.core.exceptions import ValidationError


TIPO_ACESSO = [

    ('1', 'Livre'),
    ('2', 'Restrito'),
    ('3', 'Reservado')
]

class Pessoa(models.Model):
    Nome = models.CharField('Nome', max_length=100, null=True)
    Cartao = models.CharField('Numero Cartão', max_length=15, null=True, blank=True)
    CPF = models.CharField('CPF', max_length=15, unique=True, null=True)

    def __unicode__(self):
        "%s - %s" % ( self.Nome)

class Lugar(models.Model):
    Nomelugar = models.CharField('Nome do Lugar', max_length=100, null=True)

    def __unicode__(self):
        return "%s - %s" % ( self.NomeLugar)

class TipoAcesso(models.Model):
    Nivel = models.CharField('Nivel de Acesso', max_length=1, choices=TIPO_ACESSO, null=True)

    def __unicode__(self):
        return "%s" % (self.Nivel)

class Permissao(models.Model):
    Pessoa = models.ForeignKey(Pessoa, verbose_name='Pessoa')
    Lugar = models.ForeignKey(Lugar, verbose_name='Nome do Lugar')
    TipoAcesso = models.ForeignKey(TipoAcesso, verbose_name='Nivel de Acesso')

    def __unicode__(self):
        return "%s - %s" % ( self.Permissao)

class Registro(models.Model):
    Permissao = models.ForeignKey(Permissao)
    Data = models.DateField('Data', null=True)
    HoraChegada = models.TimeField('Hora de Entrada', null=True)
    HoraSaida = models.TimeField('Hora de Saída',blank=True,null=True)
    status = models.BooleanField('Situação',default=False)

def clean(self):
		q = Acessar.objects.filter(Pessoa=self.Pessoa, HoraSaida__isnull=True)
		p.drawString ("Erro")
		if q:
			raise ValidationError("Esta Pessoa Já está em outro local")