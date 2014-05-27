from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie.authentication import SessionAuthentication

from utils.validation import ModelFormValidation

from demografia.models import Comuna


class ComunaResource(ModelResource):

    class Meta:
        queryset = Comuna.objects.all()
        resource_name = 'comuna'