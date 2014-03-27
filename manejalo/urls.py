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
from rest_framework import viewsets, routers


from usuarios.views import UsuarioViewSet

sqs = SearchQuerySet().all()
#sqs = SearchQuerySet().filter(author='john')

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'manejalo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^rest', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^search/', include('haystack.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
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

