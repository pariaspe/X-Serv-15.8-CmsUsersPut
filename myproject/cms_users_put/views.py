from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt

from .models import Pages

# Create your views here.

FORM = """
    <form action="" method="POST">
        <label for="name">Pagina:</label><br>
        <input type="text" name="name" value=""/><br>
        <label for="name">Contenido:</label><br>
        <input type="text" name="page" value=""/><br>
        <input type="submit" value="Send">
    </form>
"""

@csrf_exempt
def barra(request):
    msg = ''
    if request.method == 'POST':
        if request.user.is_authenticated():
            page = Pages(name=request.POST['name'], page=request.POST['page'])
            if page.name == '':
                pass
            else:
                try:
                    page.save()
                except IntegrityError:
                    Pages.objects.filter(name=request.POST['name']).update(page=request.POST['page'])
                    msg = 'Valor actualizado'
        else:
            msg = 'Para crear o modificar una pagina necesitas estar logeado.'

    pages = Pages.objects.all()
    lista = '<ul>'
    for page in pages:
        lista += '<li><a href="' + page.name + '">' + page.name + '</a></li>'
    lista += '</ul>'

    if request.user.is_authenticated():
        logged = 'Logged in as ' + request.user.username + '.</br>'
        logged += '<a href="logout">Logout</a>'
    else:
        logged = 'Not logged in.</br><a href="login">Login</a>'

    respuesta = '<!DOCTYPE html>'
    respuesta += '<html><body><h1>Sistema de gestión de contenidos</h1>'
    respuesta += '<p>Las paginas diponibles son:</p>' + lista + '<p>' + msg
    respuesta += '</p>' + FORM + '<p>' + logged
    respuesta += '</p></body></html>'
    return HttpResponse(respuesta)

def otro(request, recurso):
    try:
        page = Pages.objects.get(name=recurso)
        respuesta = '<!DOCTYPE html>'
        respuesta += '<html><body>' + page.page + '</body></html>'
        return HttpResponse(respuesta)
    except Pages.DoesNotExist:
        respuesta = '<!DOCTYPE html><html><body>'
        respuesta += 'La pagina ' + recurso + ' no esta guardada</body></html>'
        return HttpResponseNotFound(respuesta)
