from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from species.models import Species 

class SpeciesListView(ListView):
	model = Species 
	context_object_name = 'species_list'
	queryset = Species.objects.all()
	template_name = 'species/list_species.html'

	def get_context_data(self, **kwargs):
		context = super(SpeciesListView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		# import pdb; pdb.set_trace()
		return context

class SpeciesDetailView(DetailView):
	model = Species 
	context_object_name = 'specie_detail'
	template_name = 'species/detailview.html'
	# slug_field = 'slug'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context	


