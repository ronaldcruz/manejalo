import datetime
from haystack import indexes
from anuncio.models import Anuncio


class AnuncioIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    marca = indexes.CharField(model_attr='marca__nombre')
    modelo = indexes.CharField(model_attr='modelo__nombre')
    anio = indexes.IntegerField(model_attr='anio')


    def get_model(self):
        return Anuncio

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

    def prepare(self, object):
        self.prepared_data = super(AnuncioIndex, self).prepare(object)
        return self.prepared_data
