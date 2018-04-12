from django.contrib import admin

from species.models import ( 
	Species,Kingdom,Phylum,ClassName, Order, Family, Genus, CommonName, SpeciesImage, Category
)

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class SpeciesResource(resources.ModelResource):
	class Meta:
		model = Species 
		fields = ("id","classname__group_as__title","kingdom__title","phylum__title","classname__title","order__title",
		"family__title","genus__title","specie",
		"sciname_author","created_by__name","created_by__email","modified","created",)


# Register your models here.
class CommonNameInline(admin.StackedInline):
	model = CommonName
	max_num = 2
	#can_delete = True
	#show_change_link = True

class SpeciesImageInline(admin.StackedInline):
	model = SpeciesImage
	max_num = 3
	can_delete = True
	show_change_link = True

class CategoryFilter(admin.SimpleListFilter):
	title = 'Category'
	parameter_name = 'status_category'

	def lookups(self, request, model_admin):
		categories = [(c.classname.group_as.id,c.classname.group_as.title) 
			for c in model_admin.model.objects.select_related('classname__group_as').all()]
		return set(categories)

	def queryset(self, request, queryset):		#
		if self.value():
			#import pdb; pdb.set_trace()
			return queryset.filter(classname__group_as__id=self.value())
		return queryset


class SpeciesAdmin(ImportExportModelAdmin):
	resource_class = SpeciesResource
	list_select_related = (
		'kingdom',
		'phylum',
		'classname',
		'order',
		'family',
		'genus',
		'created_by'		
	)
	inlines = [CommonNameInline,SpeciesImageInline]

	fieldsets = [
		("Taxon Details", {"fields":["kingdom","phylum","classname",
			"order","family","genus","specie","sciname_author"]}),
		("Identification Details", {"fields":["profile_pic","basis_of_record","taxonomic_notes"]}),
	]
	readonly_fields = ("created","modified",)
	list_display = ("slug","kingdom","phylum","classname","order",
		"family","genus","specie",
		"sciname_author","created_by","modified",)
	date_hierarchy = "modified"
	list_display_links = ("slug",)
	list_filter = (CategoryFilter,)
	search_fields = ("genus__title","specie",)
	ordering = ("-modified",)
	exclude = ['created_by',]

	def get_category(self, obj):
		#import pdb; pdb.set_trace()
		return classname.group_as.title

	#https://books.agiliq.com/projects/django-admin-cookbook/en/latest/current_user.html
	def save_model(self, request, obj, form, change):
		# import pdb; pdb.set_trace()
		if not obj.created_by:
			obj.created_by = request.user
		super().save_model(request, obj, form, change)

	def queryset(self, request):
		return super(SpeciesAdmin, self).queryset(request).select_related('classname')

	
admin.site.register(Species,SpeciesAdmin)




class CommonNameAdmin(admin.ModelAdmin):
	list_select_related = (
		'species__classname__group_as',
	)
	list_display = ("name", "species","created","modified",)
	list_filter = ("created","modified",)
	search_fields = ("name",)

admin.site.register(CommonName, CommonNameAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ("title","description",)
	search_fields = ("title",)

admin.site.register(Category, CategoryAdmin)


class SpeciesImageAdmin(admin.ModelAdmin):
	list_display = ("id","species", "pic", "description")
	fields = ('image_tag',)
	readonly_fields = ('image_tag',)

admin.site.register(SpeciesImage, SpeciesImageAdmin)

admin.site.register(Kingdom)
admin.site.register(Phylum)
admin.site.register(ClassName)
admin.site.register(Order)
admin.site.register(Family)
admin.site.register(Genus)
