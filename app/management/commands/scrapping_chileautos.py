from django.core.management.base import BaseCommand, CommandError
from reserva.models import Horario
from usuarios.models import Usuario

import datetime
import random

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        self.stdout.write('Cargando')
        Horario.objects.all().delete()

        usuarios = Usuario.objects.all()
        for usuario in usuarios:
	        for delta in range(10):
	        	now = datetime.datetime.today()
	        	now = datetime.datetime(now.year, now.month, now.day, 8, 0, 0, 0)
	        	delta_days = 1440 * delta
	        	now = now + datetime.timedelta(minutes=delta_days)

	        	for hora_delta in range(0, 150, 30):

	        		horario = Horario()
	        		horario.doctor = usuario
	        		horario.fecha = now + datetime.timedelta(minutes = hora_delta)
	        		horario.estado = random.choice(['D', 'R', 'ND'])
	        		horario.save()



        self.stdout.write('Successfully closed poll')