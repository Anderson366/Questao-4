from django.db import models

grupo = (('E', 'Escola'),('P','Prédio'))

class Colecao(models.Model):
    nome = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = 'Coleções'
    def __str__(self):
        return self.nome


class Caixa(models.Model):
    numero = models.IntegerField()
    etiqueta = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)

    def __str__(self):
        return self.etiqueta

class Revista(models.Model):
    numero_edicao = models.IntegerField()
    ano = models.IntegerField()
    colecao = models.ForeignKey(Colecao, on_delete=models.CASCADE)
    caixa = models.ForeignKey(Caixa, on_delete=models.CASCADE)


class Amigo(models.Model):
    nome = models.CharField(max_length=100)
    nome_mae = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    grupo_amigo = models.CharField(max_length=100, choices=grupo)
    revistas = models.ManyToManyField(Revista, through='Emprestimo')

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    revista = models.ForeignKey(Revista, on_delete=models.CASCADE)
    amigo = models.ForeignKey(Amigo, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField()