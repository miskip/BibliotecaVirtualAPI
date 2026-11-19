
# configura la aplicación Django
from django.apps import AppConfig


class BibliotecaConfig(AppConfig):
    #establece el tipo de identificador predeterminado para los modelos
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'biblioteca'

#cuando Django termina de cargar la aplicación
    def ready(self):
        #carga las señales que crearemos
        import biblioteca.signals
