from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class Cuisine(models.Model):
    name = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='restaurant_posts')
    author_slug = models.SlugField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = CloudinaryField('image', default='default')
    rating = models.IntegerField()
    favourited = models.ManyToManyField(
        User, related_name='restaurant_favourited', blank=True)
    location = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    cuisine = models.ManyToManyField(
        Cuisine, related_name='restaurant_cuisine', blank=False)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.author_slug = slugify(self.author)
        super(Restaurant, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('restaurant_detail', kwargs={'slug': self.slug})

    def number_of_favourites(self):
        return self.favourited.count()

    def list_cuisines(self):
        cuisine_string = ""
        for cuisine in self.cuisine.all():
            cuisine_string += str(cuisine) + ", "

        return cuisine_string[:len(cuisine_string)-2]


class Comment(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    name_slug = models.SlugField(max_length=100)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
    
    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return f"Comment {self.content} by {self.name}"


class Dish(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
