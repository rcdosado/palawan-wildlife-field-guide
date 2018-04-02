from django.contrib import admin
from species.models import ( 
	Species,Kingdom,Phylum,ClassName, Order, Family, Genus, SpecieName, CommonName
)

# Register your models here.


class SpeciesAdmin(admin.ModelAdmin):
	fieldsets = [
		("Class Taxon Details", {"fields":["kingdom","phylum","classname","order","family","genus"]}),
		("Identification Details", {"fields":["specie","category","basis_of_record"]}),
	]
	readonly_fields = ("created","modified",)
	list_display = ("scientific_name","kingdom","phylum","classname","order","family","genus","specie","slug", "created","modified",)
	#list_editable = ("kingdom",)
	list_display_links = ("scientific_name",)
	list_filter = ("category","created","modified",)
	search_fields = ("kingdom","phylum","classname","order","family","genus","specie", "common_title",)
	
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
admin.site.register(SpecieName)
