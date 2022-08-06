from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Director, Pelicula

# Create your views here.

def index_peliculas(request):
    dbdata = Pelicula.objects.values_list('id','imagen','titulo','duracion','fecha_estreno', named=True).order_by('-fecha_estreno')
    context = {'peliculas' : dbdata}
    return render(request, 'peliculas.html', context)

def directores(request):
    dbdata = Director.objects.all()
    context = {
        'directores' : dbdata}
    return render(request, 'directores.html', context)

def peliporid(request, peli_id):
    data = get_object_or_404(Pelicula, id=peli_id)
    context = {'peliporid' : data}
    return render(request, 'peliporid.html',context)