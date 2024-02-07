from django.shortcuts import render, redirect

from app_coder.forms import registro_db
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
    return render(request, "app_coder/index.html", {"name": "index"})

def about(request):
    return render(request, 'app_coder/about.html',{"name": "sobre nosotros"})

def booking(request):
    return render(request, 'app_coder/booking.html',{"name": "booking"})

def contact(request):
    return render(request, 'app_coder/contact.html',{"name": "contacto"})

def room(request):
    return render(request, 'app_coder/room.html',{"name": "piezas"})

def service(request):
    return render(request, 'app_coder/service.html',{"name": "servicio"})

def team(request):
    return render(request, 'app_coder/team.html',{"name": "team"})

def testimonial(request):
    return render(request, 'app_coder/testimonial.html',{"name": "testimonio"})
