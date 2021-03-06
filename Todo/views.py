from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseRedirectBase
from django.urls import reverse
from django.shortcuts import redirect, render
from django.template import loader
from ToDo.models import Todo


def index(request):
    template = loader.get_template('ToDo/index.html')

    todo_items = Todo.objects.all().order_by("-added_date")
    context = {
        "items": todo_items
    }

    return HttpResponse(template.render(context, request))

def add_todo(request):
    content = request.POST["taskInput"]
    Todo.objects.create(text=content)

    return HttpResponseRedirect("/")

def remove_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()

    return HttpResponseRedirect("/")