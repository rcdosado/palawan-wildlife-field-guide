from django.contrib import admin
from species.models import ( 
	Species,Kingdom,Phylum,ClassName, Order, Family, Genus, CommonName, SpeciesImage
)

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

class SpeciesAdmin(admin.ModelAdmin):
	inlines = [CommonNameInline,SpeciesImageInline]

	fieldsets = [
		("Taxon Details", {"fields":["kingdom","phylum","classname","order","family","genus","specie","sciname_author"]}),
		("Identification Details", {"fields":["category","basis_of_record","taxonomic_notes"]}),
	]
	readonly_fields = ("created","modified",)
	list_display = ("slug","kingdom","phylum","classname","order","family","genus","specie","sciname_author","created","modified",)
	#list_editable = ("kingdom",)
	date_hierarchy = "modified"
	list_display_links = ("slug",)
	list_filter = ("category","created","modified",)
	search_fields = ("kingdom","phylum","classname","order","family","genus","specie", "common_title",)
	ordering = ("-modified",)

	
admin.site.register(Species,SpeciesAdmin)




class CommonNameAdmin(admin.ModelAdmin):
	list_display = ("name","scientific_name", "created","modified",)
	list_filter = ("created","modified",)
	search_fields = ("name",)

admin.site.register(CommonName, CommonNameAdmin)

admin.site.register(Kingdom)
admin.site.register(Phylum)
admin.site.register(ClassName)
admin.site.register(Order)
admin.site.register(Family)
admin.site.register(Genus)
