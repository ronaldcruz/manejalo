from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie.authentication import SessionAuthentication

from utils.validation import ModelFormValidation

from anuncio.models import Anuncio, Tipo, Marca, Modelo, Carroceria
from anuncio.forms import AnuncioForm

from demografia.api import ComunaResource

class TipoResource(ModelResource):

    class Meta:
        queryset = Tipo.objects.all()
        resource_name = 'tipo'

class MarcaResource(ModelResource):

    class Meta:
        queryset = Marca.objects.all()
        resource_name = 'marca'

class ModeloResource(ModelResource):

    class Meta:
        queryset = Modelo.objects.all()
        resource_name = 'modelo'

class CarroceriaResource(ModelResource):

    class Meta:
        queryset = Carroceria.objects.all()
        resource_name = 'carroceria'

class AnuncioResource(ModelResource):

    tipo_vehiculo = fields.ForeignKey(TipoResource, 'tipo_vehiculo', full=True)
    marca = fields.ForeignKey(MarcaResource, 'marca', full=True)
    modelo = fields.ForeignKey(ModeloResource, 'modelo', full=True)
    carroceria = fields.ForeignKey(CarroceriaResource, 'carroceria', full=True)

    comuna = fields.ForeignKey(ComunaResource, 'comuna', full=True)

    class Meta:
        queryset = Anuncio.objects.all()
        resource_name = 'anuncio'
        validation = ModelFormValidation(form_class=AnuncioForm)
        authorization = Authorization()
        always_return_data=True

    def hydrate_marca(self, bundle):
        if isinstance(bundle.data['marca'], int):
            bundle.data['marca'] = '/api/marca/{0}/'.format(bundle.data['marca'])
        return bundle

    def hydrate_modelo(self, bundle):
        if isinstance(bundle.data['modelo'], int):
            bundle.data['modelo'] = '/api/modelo/{0}/'.format(bundle.data['modelo'])
        return bundle

    def hydrate_carroceria(self, bundle):
        if isinstance(bundle.data['carroceria'], int):
            bundle.data['carroceria'] = '/api/carroceria/{0}/'.format(bundle.data['carroceria'])
        return bundle

    def hydrate_tipo_vehiculo(self, bundle):
        if isinstance(bundle.data['tipo_vehiculo'], int):
            bundle.data['tipo_vehiculo'] = '/api/tipo/{0}/'.format(bundle.data['tipo_vehiculo'])
        return bundle

    def hydrate_comuna(self, bundle):
        if isinstance(bundle.data['comuna'], int):
            bundle.data['comuna'] = '/api/comuna/{0}/'.format(bundle.data['comuna'])
        return bundle    