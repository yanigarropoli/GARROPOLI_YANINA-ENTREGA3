from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from usuarios.forms import NuestroUserCreationForm, NuestroUserChangeForm
from django.contrib.auth import login as django_login
from usuarios.models import InfoExtra
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.models import User



def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            django_login(request, usuario)
            
            InfoExtra.objects.get_or_create(user=usuario)
            
            return redirect('inicio')
    else:
        formulario = AuthenticationForm()
    
    return render(request, 'usuarios/login.html', {'formulario': formulario})

def registro(request):
    
    if request.method == 'POST':
        formulario = NuestroUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = NuestroUserCreationForm()
    return render(request, 'usuarios/registrar.html', {'formulario': formulario})


@login_required
def perfil(request):
 
    info_extra = request.user.infoextra
    
    if request.method == 'POST':
        form = NuestroUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            
            if form.cleaned_data.get('avatar'):
                info_extra.avatar = form.cleaned_data.get('avatar')
            
            if form.cleaned_data.get('hobbies'):
                info_extra.hobbies = form.cleaned_data.get('hobbies')
            
        
            
            info_extra.save()
            
            form.save()
            return redirect('editar_perfil')
    else:
      form= NuestroUserChangeForm(instance=request.user, initial={'avatar': info_extra.avatar,'hobbies': info_extra.hobbies})
    return render(request, 'usuarios/perfil.html', {'form': form})




class editar_perfil(UpdateView):
    model =User
    template_name = 'usuarios/editar_perfil.html'  
    success_url = reverse_lazy('perfil')  
    fields= ['email', 'first_name', 'last_name']

    def get_object(self):
        return self.request.user
