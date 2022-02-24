from django.db import models, IntegrityError
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """
    The Profile model is linked to the Django User model and is used to
    allow the registered user's to have a profile which they can edit.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    location = models.CharField(max_length=200, blank=True)
    favourite_cuisine = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    image = CloudinaryField('image', default='default')

    def save(self, *args, **kwargs):
        try:
            self.slug = slugify(str(self.user))
            super(Profile, self).save(*args, **kwargs)
        except IntegrityError:
            latest = Profile.objects.latest('id')
            next_id = latest.id + 1
            self.slug = slugify(str(self.user) + str(next_id))
            super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})
