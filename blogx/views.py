from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import my_item




def show_blogx(request):
    return render(request,"blogx.html",{"entry": my_item})


def get_blogx(request, todo_id):
    try:
        return HttpResponse(my_item[int(todo_id)])
    except IndexError:
        raise Http404("We don't have any.")

