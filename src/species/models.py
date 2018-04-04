from django.db import models
from django_extensions.db.fields import (
	AutoSlugField, CreationDateTimeField, ModificationDateTimeField,
)

class Category(models.Model):
	title = models.CharField(max_length=40,
		help_text="Write which group this animal belongs to, relative to species's class e.g aves for birds")
	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'
	def __str__(self):
		return self.title	

class Kingdom(models.Model):
	title = models.CharField(max_length=40,
		help_text="The full scientific name of the kingdom in which the taxon is classified. Example: \"Animalia\", \"Plantae\"")
	description = models.TextField(blank=True)

	class Meta:
		verbose_name = 'Kingdom'
		verbose_name_plural = 'Kingdoms'

	def __str__(self):
		return self.title


class Phylum(models.Model):
	title = models.CharField(max_length=40,
		help_text="The full scientific name of the phylum or division in which the taxon is classified.")
	description = models.TextField(blank=True)

	class Meta:
		verbose_name = 'Phylum'
		verbose_name_plural = 'Phyla'

	def __str__(self):
		return self.title

class ClassName(models.Model):
	title = models.CharField(max_length=40,
		help_text="The full scientific name of the class in which the taxon is classified.")
	group_as = models.ForeignKey(Category,blank=True,null=True,verbose_name="Categorize as",
		help_text="term used by many to easily identify this species e.g Aves is to birds, ")
	description = models.TextField(blank=True)

	class Meta:
		verbose_name = 'Class'
		verbose_name_plural = 'Classes'

	def __str__(self):
		return self.title

class Order(models.Model):
	title = models.CharField(max_length=40,
		help_text="The full scientific name of the order in which the taxon is classified.")
	description = models.TextField(blank=True)

	class Meta:
		verbose_name = 'Order'
		verbose_name_plural = 'Orders'

	def __str__(self):
		return self.title

class Family(models.Model):
	title = models.CharField(max_length=40,
		help_text="The full scientific name of the family in which the taxon is classified.")
	description = models.TextField(blank=True)

	class Meta:
		verbose_name = 'Family'
		verbose_name_plural = 'Families'

	def __str__(self):
		return self.title

class Genus(models.Model):
	title = models.CharField(max_length=40,
		help_text="The full scientific name of the genus in which the taxon is classified")
	description = models.TextField(blank=True)

	class Meta:
		verbose_name = 'Genus'
		verbose_name_plural = 'Genera'


	def __str__(self):
		return self.title

class Species(models.Model):
	RECORD_BASIS = (
		('','-----------'),
		('hob','HumanObservation'),
		('lis','LivingSpeciment'),
		('prs','PreservedSpecimen'),
		('fos','FossilSpecimen'),
		('mob','MachineObservation'),
	)

	kingdom = models.ForeignKey(Kingdom,
		help_text="The full scientific name of the kingdom in which the taxon is classified. Example: \"Animalia\", \"Plantae\"")
	phylum = models.ForeignKey(Phylum,
		help_text="The full scientific name of the phylum or division in which the taxon is classified.")
	classname = models.ForeignKey(ClassName,
		help_text="The full scientific name of the class in which the taxon is classified.",
		verbose_name="class")
	order = models.ForeignKey(Order,
		help_text="The full scientific name of the order in which the taxon is classified.")
	family = models.ForeignKey(Family,
		help_text="The full scientific name of the family in which the taxon is classified.")
	genus = models.ForeignKey(Genus,
		help_text="The full scientific name of the genus in which the taxon is classified")
	specie = models.CharField(max_length=80,verbose_name="Species",
		help_text="Species name of this species, ex. Familiaris, from Canis Familiaris.")
	sciname_author = models.CharField(max_length=80,verbose_name="Scientific name author")
	basis_of_record = models.CharField(max_length=3,verbose_name="record basis",
		choices=RECORD_BASIS,default='hob',
		help_text="The specific nature of the data record - a subtype of the dcterms:type. ")
	slug = AutoSlugField(populate_from=['genus','specie'],verbose_name="Name")
	taxonomic_notes = models.TextField(help_text="Any notes you wan to add about this species",blank=True)
	created = CreationDateTimeField()
	modified = ModificationDateTimeField()

	class Meta:
		verbose_name = 'species'
		verbose_name_plural = 'species'


	def __str__(self):
		return self.get_full_name()

	@property
	def scientific_name(self):
		return self.get_full_name()


	def get_full_name(self):
		return self.family.title+' '+self.specie

class CommonName(models.Model):
	name = models.CharField(max_length=80)
	species = models.ForeignKey(Species, related_name='common_name', on_delete=models.CASCADE)
	created = CreationDateTimeField()
	modified = ModificationDateTimeField()

	@property
	def scientific_name(self):
		#import pdb; pdb.set_trace()
		return self.species.scientific_name

	def __str__(self):
		return self.name

class SpeciesImage(models.Model):
	species = models.ForeignKey(Species,help_text="Add your species image(s) here")
	image = models.ImageField('Species Image',upload_to='species_pics/%Y-%m-%d/',null=True,blank=True)
	description = models.TextField(blank=True,help_text="Any description of the image e.g attribution, location etc.")

	def __str__(self):
		return self.species.scientific_name




