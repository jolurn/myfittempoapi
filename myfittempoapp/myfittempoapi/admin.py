from django.contrib import admin
from myfittempoapi.models import Cliente,Empleado,Oferta,Carrito

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
  list_display = ('primerNombre','segundoNombre','apellidoPaterno','apellidoMaterno','dni','celular','correo','password','direccion','fechaRegistro')

admin.site.register(Cliente,ClienteAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
  list_display = ('primerNombre','segundoNombre','apellidoPaterno','apellidoMaterno','dni','celular','correo','password','direccion','distrito','profesión','descripcion','fotoPerfil','fotoBanner','video','fechaRegistro')

admin.site.register(Empleado,EmpleadoAdmin)

class OfertaAdmin(admin.ModelAdmin):
  list_display = ('empleado','fechaOferta','horaInicio','horaFin','costo','estadoOferta','fechaRegistro')

admin.site.register(Oferta,OfertaAdmin)

class CarritoAdmin(admin.ModelAdmin):
  pass
  # list_display = ('idCarrito','cliente','estadoCarrito','estado','fechaRegistro')

# admin.site.register(Carrito,CarritoAdmin)