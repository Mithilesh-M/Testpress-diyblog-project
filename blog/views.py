from django.shortcuts import render
from .models import Blog, Blogger, Comment



def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blogs = Blog.objects.all().count()
    num_bloggers = Blogger.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
