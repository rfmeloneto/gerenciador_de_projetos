from django.core.exceptions import ValidationError
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    projects = models.ManyToManyField('Project', related_name='users_enrroled', blank=True)

    def clean(self):
        if self.projects.count() > 3:
            raise ValidationError('Um usuário não pode ter mais de 3 projetos.')

    def __str__(self):
        return self.name
    
    def add_project(self, project):
        through_defaults = {'id': None}
        self.projects.add(project, through_defaults=through_defaults)
    



class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    users = models.ManyToManyField('User', related_name='users_projects', blank=True)

    def clean(self):
        if self.users.count() > 5:
            raise ValidationError('Um projeto não pode ter mais de 5 usuários.')

    def __str__(self):
        return self.name
    
    def add_user(self, user):
        through_defaults = {'id': None}
        self.users.add(user, through_defaults=through_defaults)

