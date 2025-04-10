from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte automatiquement l'utilisateur après l'inscription
            return redirect('dashboard')  # Redirige vers le tableau de bord ou une autre page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')