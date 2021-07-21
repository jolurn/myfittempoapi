"""myfittempoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myfittempoapi.views import LoginAPI
from myfittempoapi.viewsets import ClienteViewset, EmpleadoViewset, OfertaViewset,CarritoViewset,MercadopagoViewset,UsuarioViewset,EmpleadoUsuarioViewset
from django.conf import settings
from myfittempoapi.controllers.empleado_imagen_controller import EmpleadoImagenController
from django.conf.urls.static import static


urlpatterns = [
    path('login',LoginAPI.as_view()),
    path('admin/', admin.site.urls),
    path('empleado/imagen/upload',EmpleadoImagenController.as_view()),
    path('user', UsuarioViewset.as_view({'get':'listar','post':'create'})),    
    path('user_cliente', UsuarioViewset.as_view({'get':'listar_usuario_activo','post':'create_usu_cliente'})),
    path('mercadopago', MercadopagoViewset.as_view({'post':'create'})),
    path('clientes',ClienteViewset.as_view({'get':'listar','post':'create'})),
    path('cliente/<id>',ClienteViewset.as_view({'get':'retrieve','put':'update'})),
    path('empleados',EmpleadoViewset.as_view({'get':'listar','post':'create'})),
    path('empleado/<id>',EmpleadoViewset.as_view({'get':'retrieve','put':'update'})),
    path('usu_empleado/<id>',EmpleadoUsuarioViewset.as_view({'get':'listar_empleado_id_usuario'})),
    path('oferta',OfertaViewset.as_view({'get':'listar_activos','post':'create'})),
    path('ofertas_empleado/<id>',OfertaViewset.as_view({'get':'listar_oferta_por_trabajador','put':'delete'})),
    path('oferta_one/<id>',OfertaViewset.as_view({'get':'retrieve'})),
    path('oferta/<id>',OfertaViewset.as_view({'get':'retrieve','put':'update'})),
    path('carritos',CarritoViewset.as_view({'get':'listar','post':'create'})),
    path('carrito/<id>',CarritoViewset.as_view({'get':'retrieve'})),
    # path('tokenize',TokenizeViewset.as_view({'post':'get_token'}))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)