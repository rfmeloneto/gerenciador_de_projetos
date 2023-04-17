from django.shortcuts import redirect, render
from rest_framework import generics

from .forms import AssociateForm, ProjectForm, UserForm
from .models import Project, User
from .serializers import ProjectSerializer, UserSerializer


def home(request):  #View ok
    return render(request, 'home.html')

def user_create(request):  #View ok
    if request.method == 'POST':
       form = UserForm(request.POST)
       if form.is_valid():
           user = form.save(commit=False)
           user.save()
           return redirect('user_list')
    else:
       form = UserForm()

    return render(request, 'user_create.html', {'form': form})


def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('project_list')
    else:
        form = ProjectForm()

    return render(request, 'project_create.html', {'form': form})



def user_list(request): #View ok
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users,})



def project_list(request): #View ok
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects,})


def user_project_associate(request):
    if request.method == 'POST':
        form = AssociateForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data['project']
            users = form.cleaned_data['users']
            for user in users:
                project.add_user(user)
            return redirect('project_list')
    else:
        form = AssociateForm()
    return render(request, 'user_project_associate.html', {'form': form})

def edit_project(request,id):
    project= Project.objects.get(id=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form})

def delete_project(request,id):
    project= Project.objects.get(id=id)
    if request.method == 'POST':
            project.delete()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'delete_project.html', {'project': project})

##### API VIEWS #####

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ProjectListAPIView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()



