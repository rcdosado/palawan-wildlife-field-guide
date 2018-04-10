from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from project_msit.settings import base

from species.models import Species,Category

class SpeciesListView(ListView):
	model = Species 
	queryset = Species.objects.select_related('classname__group_as',
		'kingdom','phylum','order','family','genus','created_by').all().order_by('-modified')		
	template_name = 'species/list_species.html'

	def get_context_data(self, **kwargs):
		context = super(SpeciesListView, self).get_context_data(**kwargs)
		# context['now'] = timezone.now()
		context['category_list'] = Category.objects.all()
		return context

class SpeciesDetailView(DetailView):
	model = Species 
	context_object_name = 'specie_detail'
	template_name = 'species/detailview.html'
	# slug_field = 'slug'

	def get_queryset(self):
		#import pdb; pdb.set_trace()
		if 'pk' in self.kwargs:
			return Species.objects.select_related('classname__group_as','kingdom',
				'phylum','order','family','genus','created_by').filter(id=self.kwargs['pk'])
		return None		

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# import pdb; pdb.set_trace()
		# context['now'] = timezone.now()
		#import pdb; pdb.set_trace()
		context['category_list'] = Category.objects.all().order_by('title')
		return context	


