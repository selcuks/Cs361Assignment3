from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from tags.models import Tag
from .models import blogxx
from .forms import blogxForm

def show_blogx(request):

    if request.method == "POST":
        formx = blogxForm(request.POST)
        if formx.is_valid():
            blogx = formx.save(commit=False)
            blogx.owner_s = request.user
            blogx.save()
            formx.save_m2m()

    elif request.method == "GET":
        formx = blogxForm()

    return render(request, "my_blogs.html", {"blogxxx": blogxx.objects.filter(owner_s=request.user.id),
                                             "tags_s":Tag.objects.all(),
                                             "formx": formx})


def get_blogx(request, blogx_id):
    try:
        blogx = blogxx.objects.get(id=blogx_id)
        if request.user.id != blogx.owner_s.id:
            raise PermissionDenied
        return render(request, "detailed_blogss.html", {"blogx": blogx})
    except blogxx.DoesNotExist:
        raise Http404("We don't have any.")