from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    #----------------------------------------------------------------------------------------HOME
    path('', home, name="home"),
    #----------------------------------------------------------------------------------------LOGIN, LOGOUT
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="AppSpec/home.html"), name="logout"),
    #----------------------------------------------------------------------------------------SELECCIONAR, IMPORTAR, CARGAR EXCEL
    path('seleccionar_archivo/', seleccionar_archivo, name='seleccionarArchivo'),
    path('importar/', import_excel, name='import_excel'),
    #path('cargar_excel/', cargar_excel, name='cargar_excel'),
    #----------------------------------------------------------------------------------------AREAS
    path('areas/', AreaList.as_view(), name="areas"),
    path('areas_create/', AreaCreate.as_view(), name="areas_create"),
    path('areas_update/<int:pk>/', AreaUpdate.as_view(), name="areas_update"),
    path('areas_delete/<int:pk>/', AreaDelete.as_view(), name="areas_delete"),
    #----------------------------------------------------------------------------------------PERSONAS
    path('personas/', PersonaList.as_view(), name="personas"),
    path('personas_create/', PersonaCreate.as_view(), name="personas_create"),
    path('personas_update/<int:pk>/', PersonaUpdate.as_view(), name="personas_update"),
    path('personas_delete/<int:pk>/', PersonaDelete.as_view(), name="personas_delete"),
    path('buscar_personas/', buscar_personas, name="buscar_personas"),
    #----------------------------------------------------------------------------------------PERSONAS POR AREA
    path('obtener_personas_area/', obtener_personas_area, name='obtener_personas_area'),
    ]