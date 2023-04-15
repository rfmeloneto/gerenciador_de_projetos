from django.shortcuts import render, redirect
from .forms import UserForm, ProjectForm, AssociateForm
from .models import User, Project
from .models import User, Project
from .serializers import UserSerializer, ProjectSerializer, AssociateSerializer, DisassociateSerializer
from rest_framework import generics


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


'''
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()  
            form.save_m2m()  
            return redirect('project_list')
    else:
        form = ProjectForm()

    return render(request, 'project_create.html', {'form': form})
'''
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
    projects = Project.objects.all()
    return render(request, 'user_list.html', {'users': users, 'projects':projects})



def project_list(request): #View ok
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

'''
def user_project_associate(request):  #View ok
    if request.method == 'POST':
        form = AssociateForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            project_id = form.cleaned_data['project_id']
            user = User.objects.get(pk=user_id)
            project = Project.objects.get(pk=project_id)

            if user.projects.count() >= 3:
                form.add_error(None, 'Este usuário já está em 3 projetos.')
            elif project.users.count() >= 5:
                form.add_error(None, 'Este projeto já tem 5 usuários.')
            else:
                user.projects.add(project)
                return redirect('user_list')
    else:
        form = AssociateForm()

    return render(request, 'user_project_associate.html', {'form': form})
'''
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


##### API VIEWS #####

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserSearchAPIView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        name = self.request.query_params.get('name', None)
        email = self.request.query_params.get('email', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if email:
            queryset = queryset.filter(email__icontains=email)
        return queryset

class ProjectListAPIView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class ProjectSearchAPIView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
class UserDetailAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ProjectDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class UserProjectAssociateAPIView(generics.UpdateAPIView):
    serializer_class = AssociateSerializer
    queryset = Project.objects.all()

class UserProjectDisassociateAPIView(generics.UpdateAPIView):
    serializer_class = DisassociateSerializer
    queryset = Project.objects.all()

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

class ProjectCreateAPIView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
