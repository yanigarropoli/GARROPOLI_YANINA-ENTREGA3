from django.urls import path
from inicio.views import inicio, cargar_vinos, listar_vinos, filtrar_vinos, detalle_vinos

urlpatterns = [
    path('', inicio, name="inicio"),
    path('cargar-vinos/', cargar_vinos, name="cargar_vinos"),
    path('listar-vinos/', listar_vinos, name="listar_vinos"),
    path('filtrar-vinos/', filtrar_vinos, name="filtrar_vinos"),
    path('ver-vinos/<int:id>/', detalle_vinos, name="detalle_vinos"),
    
   

    
 
    
]