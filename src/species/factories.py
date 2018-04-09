import factory
import random, string
# from django.contrib.auth import get_user_model
from profiles.factories import UserFactory,ProfileFactory
from .models import ( 
	Kingdom,Phylum,ClassName, Order, Family, Genus, CommonName, SpeciesImage, Category,Species
)


def random_string(count=4):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(count))

# email = factory.Sequence(lambda n: "test{0}%s@gmail.com".format(n) % random_string())

class KingdomFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Kingdom

	title = factory.Sequence(lambda n: "%s_kingdom".format(n) % random_string())

class PhylumFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Phylum

	title = factory.Sequence(lambda n: "%s_phylum".format(n) % random_string())



class OrderFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Order

	title = factory.Sequence(lambda n: "%s_order".format(n) % random_string())

class FamilyFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Family

	title = factory.Sequence(lambda n: "%s_family".format(n) % random_string())

class GenusFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Genus

	title = factory.Sequence(lambda n: "%s_genus".format(n) % random_string())

class CategoryFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Category

	title = factory.Sequence(lambda n: "%s_category".format(n) % random_string())

class ClassNameFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = ClassName

	title = factory.Sequence(lambda n: "%s_class".format(n) % random_string())
	group_as = factory.SubFactory(CategoryFactory)


class SpeciesFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Species

	kingdom = factory.SubFactory(KingdomFactory)
	phylum = factory.SubFactory(PhylumFactory)
	classname = factory.SubFactory(ClassNameFactory)
	order = factory.SubFactory(OrderFactory)
	family = factory.SubFactory(FamilyFactory)
	genus = factory.SubFactory(GenusFactory)
	specie = factory.Sequence(lambda n: 'Specie %d' % n)
	sciname_author = factory.Sequence(lambda n: 'Scientist %d' % n)
	basis_of_record = factory.Iterator(Species.RECORD_BASIS, getter=lambda c: c[0])
	created_by = factory.SubFactory(UserFactory)
