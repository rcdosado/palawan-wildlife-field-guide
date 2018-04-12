from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.db.models import Q
from project_msit.settings import base

from species.models import Species,Category,SpeciesImage

class SpeciesListView(ListView):
	model = Species 
	queryset = Species.objects.select_related('classname__group_as',
		'kingdom','phylum','order','family','genus','created_by').all().order_by('-modified')		
	template_name = 'species/list_species.html'
	paginate_by=4


	def get_queryset(self):
		'''
			we simply override the queryset, and get the default queryset(that one above), 
			and filter it according to parameters from users
			we use Q object for this
		'''
		qs = super(SpeciesListView, self).get_queryset()
		user_query = self.request.GET.get("q")
		user_filter = self.request.GET.get("search_param")
		# import pdb; pdb.set_trace()
		if user_query:
			user_query=user_query.strip()
			return qs.filter(
				Q(kingdom__title__icontains=user_query) |
				Q(phylum__title__icontains=user_query) |
				Q(order__title__icontains=user_query) |
				Q(family__title__icontains=user_query) |
				Q(genus__title__icontains=user_query) |
				Q(specie__icontains=user_query) |
				Q(sciname_author__icontains=user_query) |
				Q(classname__group_as__title__icontains=user_query) |
				Q(created_by__name__icontains=user_query) 
			)
		return qs 

	def get_context_data(self, **kwargs):
		context = super(SpeciesListView, self).get_context_data(**kwargs)
		# context['now'] = timezone.now()
		# use annotation here, some duplicate query detected
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
		# context['now'] = timezone.now()
		context['category_list'] = Category.objects.all().order_by('title')
		spqs = SpeciesImage.objects.filter(species__id=self.kwargs['pk'])
		context['image_urls'] = [s.pic.url for s in spqs]
		# import pdb; pdb.set_trace()
		return context	


