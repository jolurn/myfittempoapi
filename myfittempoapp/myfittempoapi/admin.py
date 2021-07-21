from django.contrib import admin
from myfittempoapi.models import Cliente,Empleado,Oferta,Carrito,User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
  list_display = ('username','primerNombre','segundoNombre','apellidoPaterno','apellidoMaterno','dni','celular','email','password','direccion')
 
admin.site.register(User,UserAdmin)

class ClienteAdmin(admin.ModelAdmin):
  pass

admin.site.register(Cliente,ClienteAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
  list_display = ('usuarios','distrito','profesion','descripcion','fotoPerfil','fotoBanner','video','estado','fechaRegistro')
  
admin.site.register(Empleado,EmpleadoAdmin)

class OfertaAdmin(admin.ModelAdmin):
  list_display = ('empleado','fechaOferta','horaInicio','horaFin','costo','estadoOferta','estadoOferta','estado','fechaRegistro')
  
admin.site.register(Oferta,OfertaAdmin)

class CarritoAdmin(admin.ModelAdmin): 
  # list_display = ('cliente','estadoCarrito','estadoCarrito','estado','fechaRegistro')
  pass

admin.site.register(Carrito,CarritoAdmin)