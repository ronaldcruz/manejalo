from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView
from usuarios.models import Usuario
from anuncio.forms import AnuncioSearchForm
from anuncio.api import AnuncioResource, MarcaResource, ModeloResource, CarroceriaResource, TipoResource
from demografia.api import ComunaResource


anuncio_resource = AnuncioResource()
marca_resource = MarcaResource()
modelo_resource = ModeloResource()
carroceria_resource = CarroceriaResource()
tipo_resource = CarroceriaResource()
comuna_resource = ComunaResource()

sqs = SearchQuerySet().all()
#sqs = SearchQuerySet().filter(author='john')

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'manejalo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^rest', include(router.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    (r'^api/', include(anuncio_resource.urls)),
    (r'^api/', include(marca_resource.urls)),
    (r'^api/', include(modelo_resource.urls)),
    (r'^api/', include(carroceria_resource.urls)),
    (r'^api/', include(tipo_resource.urls)),
    (r'^api/', include(comuna_resource.urls)),
    
    #url(r'^search/', include('haystack.urls')),
)

urlpatterns += patterns('haystack.views',
    url(r'^search', SearchView(
        template='search/search.html',
        searchqueryset=sqs,
        form_class=AnuncioSearchForm
    ), name='haystack_search'),
)


urlpatterns += patterns('app.views',
    url(r'^$', 'home', name='home'),
)


urlpatterns += patterns('usuarios.views',
    url(r'^login', 'login', name='login'),
    url(r'^signup', 'signup', name='signup'),
    url(r'^recovery', 'recovery', name='recovery'),
)

urlpatterns += patterns('anuncio.views',
    url(r'^advertisement/(?P<anuncio_id>\d+)$', 'show', name='advertisement_show'),
    url(r'^advertisement/new$', 'create', name='advertisement_create'),
)

urlpatterns += patterns('anuncio.search',
    url(r'^resultados$', 'search', name='search'),
)


urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

