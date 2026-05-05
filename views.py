from django.shortcuts import render
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm
from .models import Post

def inicio(request):
    return render(request, "inicio.html")


def crear_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "form.html", {"form": form, "titulo": "Crear Autor"})


def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "form.html", {"form": form, "titulo": "Crear Categoria"})


def crear_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "form.html", {"form": form, "titulo": "Crear Post"})


def buscar_post(request):
    resultados = []
    if request.GET.get("titulo"):
        titulo = request.GET["titulo"]
        resultados = Post.objects.filter(titulo__icontains=titulo)

    form = BusquedaPostForm()

    return render(request, "buscar.html", {"form": form, "resultados": resultados})