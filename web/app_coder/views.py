from django.shortcuts import render, redirect

from app_coder.models import registro_db
# Create your views here.

def autor_create_view(request):
    form = registro_db(request.POST or None)
    if form.is_valid():
        form.save()
        form = registro_db()
        template_index = 'index.html'
        context = {'form':form}
        return render(request, template_index,context)
    else:
        form = registro_db()
        return render(request, 'index.html', {'form':form})


def inicio(request):
    return render(request, "app_coder/index.html")