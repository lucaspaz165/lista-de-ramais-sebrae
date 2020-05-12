from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Unidade(models.Model):
    nome_completo = models.CharField(name='nome_completo', max_length=70, null=True, blank=False)
    sigla = models.CharField(max_length=10, null=False, blank=False)
    descrição = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.sigla


funcoes = (('Estagiário(a)', 'Estagiário(a)'), ('Funcionário(a)', 'Funcionário(a)'), ('Temporário(a)', 'Temporário(a)'),
     ('Terceirizado(a)', 'Terceirizado(a)'))


class Ramais(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique= True)
    nome = models.CharField(max_length=100, null=True, blank=False, unique=True)
    ramal = models.DecimalField(max_digits=4, decimal_places=0, blank=False, unique=True)
    unidade = models.ForeignKey('Unidade', on_delete='CASCADE', null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    whatsapp = models.CharField('whatsapp', max_length=15, null=True, blank=True)
    dia_de_nascimento = models.DecimalField('Dia de nascimento', decimal_places=0, max_digits=2, validators=[MinValueValidator(1)] and [MaxValueValidator(31)], null=True, blank=False)
    mes_de_nascimento = models.DecimalField('Mês de nascimento', decimal_places=0, max_digits=2, validators=[MinValueValidator(1)] and [MaxValueValidator(12)], null=True, blank=False)
    foto = models.ImageField(upload_to="%Y/%m/%d/", null=True, blank=True)
    funcao = models.CharField('Função' ,max_length=25, choices=funcoes, null=True, blank=False, name='Função')
    admin = models.BooleanField (max_length = 10, null=True, blank=True, )

    def clean(self):
        if self.whatsapp is None:
            self.whatsapp = 'Não informado'

    def __str__(self):

        return f' {self.nome}'
