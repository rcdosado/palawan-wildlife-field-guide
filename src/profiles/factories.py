import factory
import random, string
from django.contrib.auth import get_user_model
from .models import Profile


def random_string(count=4):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(count))

class UserFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = get_user_model()

	name = factory.Faker('name')
	email = factory.Sequence(lambda n: "test{0}%s@gmail.com".format(n) % random_string())


class ProfileFactory(factory.django.DjangoModelFactory):
	"""
	Creates a standard user.
	"""
	class Meta:
		model = Profile

	user = factory.SubFactory(UserFactory)
