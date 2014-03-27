from django import forms
from haystack.forms import SearchForm
from anuncio.models import Anuncio

class AnuncioForm(forms.ModelForm):

    #marca = forms.ForeignKey(Marca)
    #modelo = forms.ForeignKey(Modelo)
    version = forms.CharField(max_length=200)
    anio = forms.IntegerField()
    patente = forms.CharField(max_length=10)
    tipo_vehiculo = forms.CharField(max_length=100)
    carroceria = forms.CharField(max_length=100)
    kilometraje = forms.IntegerField()
    cilindrada = forms.CharField(max_length=100)
    color = forms.CharField(max_length=50)
    #imagen = StdImageField(upload_to='anuncios', blank=True, variations={'large': (640, 480, True), 'thumbnail': (125, 100, True)})
    precio = forms.IntegerField()

    tranmision_automatico = forms.BooleanField(widget=forms.CheckboxInput())
    doble_traccion = forms.BooleanField(widget=forms.CheckboxInput())
    alarma = forms.BooleanField(widget=forms.CheckboxInput())
    alzavidrios_electricos = forms.BooleanField(widget=forms.CheckboxInput())
    aire_acondicionado = forms.BooleanField(widget=forms.CheckboxInput())
    catalitico = forms.BooleanField(widget=forms.CheckboxInput())
    cierre_centralizado = forms.BooleanField(widget=forms.CheckboxInput())
    espejos_electricos = forms.BooleanField(widget=forms.CheckboxInput())
    espejos_abatibles = forms.BooleanField(widget=forms.CheckboxInput())
    frenos_abs = forms.BooleanField(widget=forms.CheckboxInput())
    llantas = forms.BooleanField(widget=forms.CheckboxInput())
    radio = forms.BooleanField(widget=forms.CheckboxInput())
    sunroof = forms.BooleanField(widget=forms.CheckboxInput())

    class Meta:
        model = Anuncio

class AnuncioSearchForm(SearchForm):
    q = forms.CharField(required=False)
    
    def search(self):
        # First, store the SearchQuerySet received from other processing.
        sqs = super(AnuncioSearchForm, self).search()

        print 'searching...'

        print 'self.is_valid() : ', self.is_valid()

        print 'self.data : ', self

        if not self.is_valid():
            print 'errrores en el formulario'
            return self.no_query_found()

        print self.cleaned_data['q']

        sqs = self.searchqueryset.auto_query(self.cleaned_data['q'])

        print sqs

        return sqs

    