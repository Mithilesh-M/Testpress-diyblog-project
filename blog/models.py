from django.db import models
from django.urls import reverse


class Blog(models.Model):
    """Model representing a blog"""
    title = models.CharField(max_length=200, null=False, blank=False)
    post_date = models.DateField(null=False, blank=False)
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('blog-detail', args=[str(self.id)])


class Blogger(models.Model):
    """Model representing a blogger"""
    name = models.CharField(max_length=200, null=False, blank=False)
    bio = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('blogger-detail', args=[str(self.id)])


class Comment(models.Model):
    """Model representing a comment"""
    blog = models.ForeignKey('Blog', on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        """String for representing the Model object."""
        return self.description
