from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Categoria
from .forms import *
# Create your views here.
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required


def superuser_only(function):
    def _inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return _inner

#Vistas basadas en clases
class Index(View):
    def get(self, request):
        return render(request, 'categoria/index.html')
    def post(self, request):
        return HttpResponseForbidden()
#Vistas basadas en funciones 
@login_required
@superuser_only
#Función para cargar una categoría
def crear_categoria(request):
	#Si recibimos petición post
	if request.method == 'POST':
		#Instanciamos el form de categoria con los datos enviados
		form = CategoriaForm(request.POST)
		#Validamos el formulario
		if not form.is_valid():
			#Guardamos cambios
			context = {"form": form}
			return render(request, "categoria/crear_categoria.html", context)
		form.save()
		return redirect('administrador:IndexAdministrador')
	#Si recibimos petición get
	elif request.method == 'GET':
		#Instanciamos el formulario de agregar categoria y se lo asignamos al contexto
		form = CategoriaForm()
		context = {"form": form}
		#Cargamos el html para crear categoría
		return render(request, 'categoria/crear_categoria.html', context) 

@login_required
#Función para listar las categorías existentes
def lista_categoria(request):
	#Obtenemos el queryset de las categorías ordenadas alfabéticamente
	categorias = Categoria.objects.all().order_by('nombre_categoria')
	#Asignamos al contexto el queryset
	contexto = {'categorias': categorias}
	#Cargamos el html con la lista de categorías
	return render(request, 'categoria/lista_categorias.html',contexto)
