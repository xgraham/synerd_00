from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('synerd/index.html')

    return HttpResponse(template.render( request=request))

def login(request):
    template = loader.get_template('synerd/login.html')

    return HttpResponse(template.render( request=request))

def console(request):
    template = loader.get_template('synerd/admin.html')

    return HttpResponse(template.render( request=request))