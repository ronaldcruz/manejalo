from django import forms
from django.forms.widgets import Select
from haystack.forms import SearchForm
from demografia.models import Comuna
from anuncio.models import Anuncio, Tipo, Marca, Modelo, Carroceria
from anuncio.constants import TIPO_VEHICULO_CHOICES, DIRECCION_CHOICES, TRANSMISION_CHOICES
from form_utils.forms import BetterModelForm

from djangular.forms.angular_model import NgModelFormMixin

class AnuncioForm(NgModelFormMixin, BetterModelForm):

    marca = forms.ModelChoiceField(queryset=Marca.objects.all())
    modelo = forms.ModelChoiceField(queryset=Modelo.objects.all())
    version = forms.CharField(max_length=100)
    anio = forms.ChoiceField(widget=Select(), choices=map(lambda x: (x, x), range(2014, 1950, -1) ))
    patente = forms.CharField(max_length=10)
    tipo_vehiculo = forms.ModelChoiceField(queryset=Tipo.objects.all())
    carroceria = forms.ModelChoiceField(queryset=Carroceria.objects.all())
    kilometraje = forms.IntegerField()
    cilindrada = forms.CharField(required=False, max_length=100)
    color = forms.CharField(max_length=50)
    precio = forms.CharField()
    conversable = forms.BooleanField(initial=False, required=False)

    puertas = forms.ChoiceField(required=False, widget=Select(), choices=map(lambda x: (x, x), range(2, 5)))

    comentario = forms.CharField(required=False, widget=forms.Textarea)

    potencia = forms.CharField(required=False, max_length=50)
    motor = forms.CharField(required=False, max_length=50)
    direccion = forms.ChoiceField(required=False, widget=Select(), choices=DIRECCION_CHOICES)
    transmision = forms.ChoiceField(required=False, widget=Select(), choices=TRANSMISION_CHOICES)
    
    es_taxi = forms.BooleanField(initial=False, required=False)

    aire_acondicionado = forms.BooleanField(initial=False, required=False)
    vidrios_delanteros_elec = forms.BooleanField(initial=False, required=False)
    vidrios_traseros_elec = forms.BooleanField(initial=False, required=False)
    apertura_remota_maleta = forms.BooleanField(initial=False, required=False)
    asiento_conductor_regulable = forms.BooleanField(initial=False, required=False)
    asiento_traseros_abatible = forms.BooleanField(initial=False, required=False)
    cierre_centralizado = forms.BooleanField(initial=False, required=False)
    cierre_centralizado_mando = forms.BooleanField(initial=False, required=False)
    velocidad_crucero = forms.BooleanField(initial=False, required=False)
    espejos_exteriores_elec = forms.BooleanField(initial=False, required=False)
    espejos_exteriores_abatibles_elec = forms.BooleanField(initial=False, required=False)

    airbag_conductor = forms.BooleanField(initial=False, required=False)
    airbag_copiloto = forms.BooleanField(initial=False, required=False)
    airbag_traseros = forms.BooleanField(initial=False, required=False)
    alarma = forms.BooleanField(initial=False, required=False)
    doble_traccion = forms.BooleanField(initial=False, required=False)
    frenos_abs = forms.BooleanField(initial=False, required=False)
    inmovilizador_motor = forms.BooleanField(initial=False, required=False)
    neblineros_delanteros = forms.BooleanField(initial=False, required=False)
    neblineros_traseros = forms.BooleanField(initial=False, required=False)
    vidrios_lamina_seguridad = forms.BooleanField(initial=False, required=False)
    
    luces_xenon = forms.BooleanField(initial=False, required=False)
    barra_portamaletas = forms.BooleanField(initial=False, required=False)
    portamaleta = forms.BooleanField(initial=False, required=False)
    
    radio = forms.BooleanField(initial=False, required=False)
    radio_bluetooth = forms.BooleanField(initial=False, required=False)
    radio_auxiliar = forms.BooleanField(initial=False, required=False)
    radio_usb = forms.BooleanField(initial=False, required=False)
    radio_cd = forms.BooleanField(initial=False, required=False)
    radio_dvd = forms.BooleanField(initial=False, required=False)
    radio_pantalla = forms.BooleanField(initial=False, required=False)
    radio_mp3 = forms.BooleanField(initial=False, required=False)
    radio_sd = forms.BooleanField(initial=False, required=False)
    radio_funciones_volante = forms.BooleanField(initial=False, required=False)
    gps = forms.BooleanField(initial=False, required=False)
    
    #destacado = forms.BooleanField()
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all())

    #Imagenes

    imagen1 = forms.CharField(required=False, widget=forms.FileInput)
    imagen2 = forms.CharField(required=False, widget=forms.FileInput)
    imagen3 = forms.CharField(required=False, widget=forms.FileInput)
    imagen4 = forms.CharField(required=False, widget=forms.FileInput)
    imagen5 = forms.CharField(required=False, widget=forms.FileInput)
    imagen6 = forms.CharField(required=False, widget=forms.FileInput)

    #Contacto

    contacto_nombre = forms.CharField(max_length=100)
    contacto_correo = forms.EmailField()
    contacto_telefono_movil = forms.CharField(max_length=15)
    contacto_telefono_otro = forms.CharField(max_length=15)


    class Meta:
        model = Anuncio
        fieldsets = [   ('general', \
                            {'fields': ['unico_duenio', 'es_taxi'],
                             'legend': 'General',  
                            }
                        ),
                        ('confort', \
                            {'fields': ['aire_acondicionado',
                                        'vidrios_delanteros_elec', 
                                        'vidrios_traseros_elec', 
                                        'apertura_remota_maleta', 
                                        'asiento_conductor_regulable', 
                                        'asiento_traseros_abatible', 
                                        'cierre_centralizado', 
                                        'cierre_centralizado_mando', 
                                        'velocidad_crucero', 
                                        'espejos_exteriores_elec', 
                                        'espejos_exteriores_abatibles_elec'],
                             'legend': 'Confort',  
                            }
                        ),
                        ('seguridad', \
                            {'fields': ['airbag_conductor',
                                        'airbag_copiloto', 
                                        'airbag_traseros', 
                                        'alarma', 
                                        'doble_traccion', 
                                        'frenos_abs', 
                                        'inmovilizador_motor', 
                                        'neblineros_delanteros', 
                                        'neblineros_traseros', 
                                        'vidrios_lamina_seguridad'],
                             'legend': 'Seguridad',  
                            }
                        ),
                        ('exterior', \
                            {'fields': ['luces_xenon',
                                        'barra_portamaletas', 
                                        'portamaleta'],
                             'legend': 'Exterior',  
                            }
                        ),
                        ('multimedia', \
                            {'fields': ['radio',
                                        'radio_bluetooth',
                                        'radio_auxiliar',
                                        'radio_usb',
                                        'radio_cd',
                                        'radio_dvd',
                                        'radio_pantalla',
                                        'radio_mp3',
                                        'radio_sd',
                                        'radio_funciones_volante',
                                        'gps'],
                             'legend': 'Multimedia',  
                            }
                        )
                    ]



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

    