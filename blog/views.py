from django.shortcuts import render
from .models import Blog, Blogger, Comment
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CommentForm


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


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5


class BloggerListView(generic.ListView):
    model = Blogger


class BlogDetailView(generic.DetailView):
    model = Blog


class BloggerDetailView(generic.DetailView):
    model = Blogger


@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def Comment_blog(request, pk):
    """View function for commenting a specific blog."""

    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():
            blog.comment_set.create(description=form.cleaned_data['description'])
            return HttpResponseRedirect(reverse('blog-detail', args=(blog.id,) ))

    else:
        form = CommentForm(initial={'description': ""})

    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, 'blog/comment_form.html', context)
