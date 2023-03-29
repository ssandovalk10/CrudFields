from django.http.response import JsonResponse
from django.views import View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from apps.bancoCampos.models import FieldsBank
from django.template.defaultfilters import slugify

import json 


class FieldsBankView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #Devolver todos los registros guardados
    def get(self, request, id=0):
        if(id>0):
            camposAll = list(FieldsBank.objects.filter(id=id).values())
            if len(camposAll) >0:
                campo = camposAll[0]
                data = {'message':"Success", 'campo': campo }
            else:
                data = {'message':"Campo no encontrado" }
            
            return JsonResponse(data)
        else:
            camposAll =  list(FieldsBank.objects.values())
            if len(camposAll)>0:
                data = {'message':"Success", 'data': camposAll }
            else:
                data = {'message':"Campo no encontrado" }

        return JsonResponse(data)

    #Guardar los Registros
    def post(self, request):
        dataJson = json.loads(request.body)
        FieldsBank.objects.create(
            name=dataJson['name'],
            slug=slugify(dataJson['name']),
            fieldjson=dataJson['fieldjson']
        )        
        data = {'message':"Datos Guardados"}
        return JsonResponse(data)

    #Actualizar los Registros
    def put(self, request, id):
        jdata = json.loads(request.body)
        campo = list(FieldsBank.objects.filter(id=id).values())
        if len(campo) > 0 :
            campo = FieldsBank.objects.get(id=id)
            campo.name = jdata['name']
            campo.slug = slugify(jdata['name']),
            campo.fieldjson = jdata['fieldjson']
            campo.save()
            data = {'message':"Success"}
        else :
            data = {'message':"Campo no encontrado"}
        
        return JsonResponse(data)

    #Eliminar los Registros
    def delete():
        pass