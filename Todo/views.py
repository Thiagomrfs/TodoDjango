from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    template = loader.get_template('ToDo/index.html')
    context = {
        'teste': 1
    }
    return HttpResponse(template.render(context, request))
