from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView, View
from .models import Actividad, Categoria
from django.http import HttpResponse
from django.urls import reverse_lazy
from .utils import render_to_pdf
from .forms import ActividadForm

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_protect
# Create your views here.


class InicioView(TemplateView):
    template_name = "index.html"


class Prueba(TemplateView):
    template_name = "insertar.html"


class CrearActividad(CreateView):
    template_name = 'registrarActividad.html'
    model = Actividad
    form_class = ActividadForm

    success_url = reverse_lazy('actividades_app:add-actividad')

    @csrf_protect
    def form_valid(self, form):
        actividad = form.save()
        actividad.save()
        return super(CrearActividad, self).form_valid(form)
    success_url = reverse_lazy('actividades_app:all-activities')

class ActividadListView(ListView):
    model = Actividad
    template_name = "actividades_list.html"

    def get_queryset(self):
        palabraClave = self.request.GET.get('kword','')

        #buscar por nombre de actividad
        lista = Actividad.objects.filter(
            nombre__icontains=palabraClave 
            
        )

        #buscar actividad por fecha
        if len(lista)<1:
            lista = Actividad.objects.filter(
            fecha__icontains=palabraClave 
            
        )

        return lista


class ActividadByCategoria(ListView):
    template_name = 'actividad_categoria.html'

    def get_queryset(self):
        categoria = self.kwargs['descripcion']
        lista = Actividad.objects.filter(
            categoria__descripcion=categoria
        )
        return lista




class ActividadDetailView(DetailView):
    model = Actividad
    template_name = "detail_activity.html"

    def get_context_data(self, **kwargs):
        context = super(ActividadDetailView, self).get_context_data(**kwargs)
        return context


class ActividadUpdateView(UpdateView):
    template_name = "update.html"
    model = Actividad
    form_class = ActividadForm
    success_url = reverse_lazy('actividades_app:all-activities')


class ActividadPDF(View):
    def get(self, request, *args, **kwargs):
        actividades = Actividad.objects.all()
        data = {
            'actividades': actividades
        }
        pdf = render_to_pdf('detail_activity.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


def eliminar_actividad(self, id_actividad):
    actividad = Actividad.objects.get(id=id_actividad)
    actividad.delete()
    return redirect(reverse_lazy('actividades_app:all-activities'))


#Inicios de sesion
@csrf_protect
def login_page(request):

    if request.method=='POST': #Nos llega informacion del formulario
        username=request.POST.get('username')
        password=request.POST.get('password')


        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect(reverse_lazy('actividades_app:inicio'))
        else:
            messages.warning(request,'No te has identificado correctamente!!')

    return render(request,'login.html',{
        'title':'Identificate'
    }
    )

def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('actividades_app:inicio'))