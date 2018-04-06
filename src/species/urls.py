from django.conf.urls import url

from species.views import SpeciesListView,SpeciesDetailView

urlpatterns = [
    url(r'^detail/(?P<slug>[-\w]+)$', SpeciesDetailView.as_view(), name='species-detail'),
    url(r'^$', SpeciesListView.as_view(), name='species-list'),
]
