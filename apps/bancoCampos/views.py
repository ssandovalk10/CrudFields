from django.http.response import JsonResponse
from django.views import View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from apps.bancoCampos.models import FieldsBank

import json 


class FieldsBankView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #Devolver todos los registros guardados
    def get(self, request):
        camposAll =  FieldsBank.objects.values()
        camposAll = list(camposAll)
        data = {'message':"Success",'data': camposAll }
        return JsonResponse(data)

    #Guardar los Registros
    def post(self, request):
        dataJson = json.loads(request.body)
        FieldsBank.objects.create(
            name=dataJson['name'],
            slug=dataJson['slug'],
            fieldjson=dataJson['fieldjson']
        )
        print(dataJson['name'])      
        data = {'message':"Datos Guardados"}
        return JsonResponse(data)

    #Actualizar los Registros
    def put():
        pass

    #Eliminar los Registros
    def delete():
        pass