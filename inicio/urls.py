from django.urls import path
from inicio.views import inicio, cargar_vinos, listar_vinos, filtrar_vinos, detalle_vinos, EditarVino, BorrarVino, About_me

urlpatterns = [
    path('', inicio, name="inicio"),
    path('about-me', About_me, name="about_me"),
    path('cargar-vinos/', cargar_vinos, name="cargar_vinos"),
    path('listar-vinos/', listar_vinos, name="listar_vinos"),
    path('filtrar-vinos/', filtrar_vinos, name="filtrar_vinos"),
    path('ver-vinos/<int:id>/', detalle_vinos, name="detalle_vinos"),
    path('editar-vino/<int:pk>/', EditarVino.as_view(), name="editar_vinos"),
    path('borrar-vino<int:pk>/', BorrarVino.as_view(), name="borrar_vinos"),
    
   

    
 
    
]