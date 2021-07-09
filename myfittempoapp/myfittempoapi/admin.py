from django.contrib import admin
from myfittempoapi.models import Cliente,Empleado,Oferta,Carrito

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
  list_display = ('primerNombre','segundoNombre','apellidoPaterno','apellidoMaterno','dni','celular','correo','password','direccion','estado','fechaRegistro')

admin.site.register(Cliente,ClienteAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
  list_display = ('primerNombre','segundoNombre','apellidoPaterno','apellidoMaterno','dni','celular','correo','password','direccion','distrito','profesion','descripcion','fotoPerfil','fotoBanner','video','estado','fechaRegistro')

admin.site.register(Empleado,EmpleadoAdmin)

class OfertaAdmin(admin.ModelAdmin):
  list_display = ('empleado','fechaOferta','horaInicio','horaFin','costo','estadoOferta','estadoOferta','estado','fechaRegistro')

admin.site.register(Oferta,OfertaAdmin)

class CarritoAdmin(admin.ModelAdmin): 
  list_display = ('cliente','estadoCarrito','estadoCarrito','estado','fechaRegistro')

admin.site.register(Carrito,CarritoAdmin)