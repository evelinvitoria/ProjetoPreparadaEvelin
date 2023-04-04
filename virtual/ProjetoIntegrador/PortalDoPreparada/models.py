from django.db import models

class profissionais(models.Model):
    nome = models.CharField(
        max_length=80,
        null=False,
        blank=False)

    competencia = models.CharField(
        max_length=100,
        null=False,
        blank=False)
    

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=40,
        null=False,
        blank=False
    )
    


    def __str__(self):
        return self.nome
    
    def __str__(self):
        return self.competencia

    
