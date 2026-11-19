
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group

#post_migrate es una señal que se envía después de que se ejecuta la migración de la base de datos
@receiver(post_migrate)
def crear_grupos_usuarios(sender, **kwargs):
    #sender.name comprueba si la aplicación que envió la señal es 'biblioteca'
    if sender.name == 'biblioteca':
        #groups de usuarios que se crearán automáticamente después de la migración
        Group.objects.get_or_create(name='Visitantes')
        Group.objects.get_or_create(name='Bibliotecarios')
