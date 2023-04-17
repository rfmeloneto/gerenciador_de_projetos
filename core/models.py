from django.core.exceptions import ValidationError
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
   

    def __str__(self):
        return self.name
    
    



class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    users = models.ManyToManyField('User', related_name='users_projects', blank=True)
    descricao = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=(('Sob Controle', 'Sob Controle'), ('Atrasado', 'Atrasado'), ('Finalizado', 'Finalizado')), default='Sob Controle')
    setor = models.CharField(max_length=20, choices=(('Recursos Humanos', 'Recursos Humanos'), ('Desenvolvimento', 'Desenvolvimento'), ('Produção', 'Produção'), ('Marketing', 'Marketing')), default='Desenvolvimento')
    

    def __str__(self):
        return self.name
    
    def add_user(self, user):
        self.users.add(user)
        

