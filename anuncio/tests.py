from tastypie.test import ResourceTestCase
from django.core.urlresolvers import reverse

from anuncio.models import Marca, Modelo, Carroceria, Tipo

class AnuncioTest(ResourceTestCase):

    URL = '/api/anuncio/'

    def setUp(self):
        super(AnuncioTest, self).setUp()

        self.marca = Marca.objects.create(nombre='Kia')
        self.modelo = Modelo.objects.create(nombre='Morning', marca=self.marca)
        self.carroceria = Carroceria.objects.create(nombre='Hatchback')

        self.tipo_vehiculo = Tipo.objects.create(nombre='Automovil')



    def test_get_anuncios(self):
        response = self.api_client.get(self.URL)
        self.assertHttpOK(response)

    def test_save_anuncios_with_out_params(self):
        params = {
            'carroceria': self.carroceria.id,
            'marca': '/api/marca/%s/' %self.marca.id,
            'modelo': '/api/modelo/%s/' %self.modelo.id,
            'tipo_vehiculo': '/api/tipo/{0}/'.format(self.tipo_vehiculo.pk),
        }
        response = self.api_client.post(self.URL, data=params)
        self.assertHttpBadRequest(response)

    def test_save_anuncios_with_incomplete_params(self):
        params = {
            'carroceria': self.carroceria.id,
            'marca': '/api/marca/%s/' %self.marca.id,
            'modelo': '/api/modelo/%s/' %self.modelo.id,
            'tipo_vehiculo': '/api/tipo/{0}/'.format(self.tipo_vehiculo.pk),
        }
        response = self.api_client.post(self.URL, data=params)
        self.assertHttpBadRequest(response)

        json_response = self.deserialize(response)
        structure_expected = {'anuncio': ''}

        self.assertKeys(json_response, structure_expected)

    def test_save_anuncios_success(self):

        params = {
            'anio': 2010,
            'cilindrada': '1.200 cc',
            'color': 'Rojo',
            'comentario': '',
            'direccion': 'H',
            'kilometraje': 25000,
            'marca': '/api/marca/{0}/'.format(self.marca.pk),
            'modelo': '/api/modelo/{0}/'.format(self.modelo.pk),
            'carroceria': '/api/carroceria/{0}/'.format(self.carroceria.pk),
            'patente': 'BHFG12',
            'precio': '12500000',
            'puertas': 3,
            'tipo_vehiculo': '/api/tipo/{0}/'.format(self.tipo_vehiculo.pk),
            'transmision': 'A',
            'version': 'Version Demo',
        }
        response = self.api_client.post(self.URL, data=params)

        print '[ ', response.content, ' ]'
        self.assertHttpCreated(response)



        json_response = self.deserialize(response)
        structure_expected = {'anuncio': ''}
        self.assertKeys(json_response, structure_expected)


