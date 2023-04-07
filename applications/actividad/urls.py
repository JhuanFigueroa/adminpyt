from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name='actividades_app'
urlpatterns = [
    path('',views.InicioView.as_view(),name='inicio'),
    path('crear-actividad/', views.CrearActividad.as_view(),name='add-actividad'),
    path('ver-actividades/',views.ActividadListView.as_view(),name='all-activities'),
    path('actividades-categoria/<descripcion>',views.ActividadByCategoria.as_view(),name='actividades-categoria'),
    path('detalle-actividad/<pk>',views.ActividadDetailView.as_view(),name='activity-detail'),
    path('editar-actividad/<pk>',views.ActividadUpdateView.as_view(),name='update-activity'),
    path('pdf-activity/',views.ActividadPDF.as_view(),name='generate-pdf'),
    path('eliminar-actividad/<int:id_actividad>',views.eliminar_actividad,name='eliminar_actividad'),
    path('login',views.login_page ,name='login'),
    path('logout',views.logout_user,name='logout')
  
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)