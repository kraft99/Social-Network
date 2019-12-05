import random
import string

from django.utils.text import slugify


def random_string_generator(size = 10,chars = string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))



def unique_slug_generator(instance,new_slug = None):
	if new_slug is not None:
		slug = new_slug
	else:
		# using .lower() method for case insensitive
        # any instance.<fieldname> can be used 
		str_ = replace_all(instance.title.lower()) # <--- change per model attr here.
		slug = slugify(str_)

	Klass = instance.__class__
	qry_exists = Klass.objects.filter(slug = slug).exists()
	if qry_exists:
		new_slug = "{slug}-{randstr}".format(slug = slug,
											randstr = random_string_generator(size = 4))

		return unique_slug_generator(instance,new_slug=new_slug)
	return slug


def replace_all(text):
	rep = {
    'ı':'i',
    'ş':'s',
    'ü':'u',
    'ö':'o',
    'ğ':'g',
    'ç':'c'

	}

	for i,j in rep.items():
		text = text.replace(i,j)
	return text


