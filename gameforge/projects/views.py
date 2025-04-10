from django.shortcuts import render, redirect, get_object_or_404
from .models import GameProject
from .forms import GameProjectForm
from django.contrib.auth.decorators import login_required

@login_required
def create_project(request):
    if request.method == 'POST':
        form = GameProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = GameProjectForm()
    return render(request, 'create_project.html', {'form': form})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(GameProject, pk=pk, user=request.user)
    return render(request, 'project_detail.html', {'project': project})
