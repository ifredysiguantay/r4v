from django.contrib import admin
from unfold.admin import ModelAdmin
import requests
import json
from .models import Property,Proyect,Images
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from unfold.contrib.filters.admin import TextFilter
from django.core.validators import EMPTY_VALUES

def get_data_from_api():
   

    headers = {'X-API-KEY':'EOh1Bt9a1aiwEOaCXkrzOxDOmgUNVMGSAeMStF6W',}

    propertys_api = requests.get('https://test.controldepropiedades.com/api/propiedades/miraiz',headers=headers)

    results = json.loads(propertys_api.text)
    

    #new_property = Property()


    #for i in propertys_db
    #print(results['data'])

    for i in results['data']:
        new_proyect = None
        created_project = None
        property = None
        if 'proyecto' in i:
            #proyect_in_db = 
            #print(datetime.strptime(i['proyecto']['updated_at'], f'YYYY-MM-DD'))

            created_date_tmp = str(i['proyecto']['created_at']).split('T')
            created_date_tmp = created_date_tmp[0]

            updated_date_tmp = str(i['proyecto']['updated_at']).split('T')
            updated_date_tmp = updated_date_tmp[0]

            new_proyect = Proyect.objects.filter(id_external=i['proyecto']['id'])

            if new_proyect:
                new_proyect.update(id_external=i['proyecto']['id'],nombre_proyecto=i['proyecto']['nombre_proyecto'],direccion=i['proyecto']['direccion'],
                                  aprobacion12cuotas=i['proyecto']['aprobacion12cuotas'],tipo=i['proyecto']['tipo'],ubicacion=i['proyecto']['ubicacion'],
                                  estado=i['proyecto']['estado'],created_at=datetime.strptime(i['proyecto']['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ'),updated_at =datetime.strptime(i['proyecto']['updated_at'], '%Y-%m-%dT%H:%M:%S.%fZ'),api=True)
                created_project = Proyect.objects.get(id_external=i['proyecto']['id'])
            else:
                new_proyect = Proyect(id_external=i['proyecto']['id'],nombre_proyecto=i['proyecto']['nombre_proyecto'],direccion=i['proyecto']['direccion'],
                                  aprobacion12cuotas=i['proyecto']['aprobacion12cuotas'],tipo=i['proyecto']['tipo'],ubicacion=i['proyecto']['ubicacion'],
                                  estado=i['proyecto']['estado'],created_at=datetime.strptime(i['proyecto']['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ'),updated_at =datetime.strptime(i['proyecto']['updated_at'], '%Y-%m-%dT%H:%M:%S.%fZ'),api=True)
                new_proyect.save()
                created_project = Proyect.objects.get(id_external=i['proyecto']['id'])
  
            #new_proyect = Proyect)

            

                
       


        created_date_tmp = datetime.strptime(i['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ') if i['created_at'] !=None else None

        updated_date_tmp = datetime.strptime(i['updated_at'], '%Y-%m-%dT%H:%M:%S.%fZ') if i['updated_at'] !=None else None

        find_de_obra_tmp = datetime.strptime(i['fin_de_obra'], '%Y-%m-%d %H:%M:%S') if i['fin_de_obra'] !=None else None

        new_property = Property.objects.filter(external_id=i['id'])

    
        if new_property:
            property = new_property.first()
            new_property.update(external_id=i['id'],propiedad=i['propiedad'],area=i['area'],tipo=i['tipo'],clase_tipo=i['clase_tipo'],modelo=i['modelo'],
                              ubicacion=i['ubicacion'],estado=i['estado'],fin_de_obra=find_de_obra_tmp,fase=i['fase'],bloqueo=i['bloqueo'],
                              precio=i['precio'],precio_sugerido=i['precio_sugerido'],proyecto_id=created_project,habitaciones=i['habitaciones'],
                              baños=i['baños'],parqueos=i['parqueos'],m2construccion=i['m2construccion'],
                              largo=i['largo'],ancho=i['ancho'],año=i['año'],titulo=i['titulo'],descripcion=i['descripcion'],detalles=i['detalles'],
                              descripcion_corta=i['descripcion_corta'],caracteristicas=i['caracteristicas'],latitud=i['latitud'],longitud=i['longitud'],
                              comision_referencia=i['comision_referencia'],comision_directa=i['comision_directa'],created_at=created_date_tmp,updated_at=updated_date_tmp,
                              api=True)

        else:
            new_property = Property(external_id=i['id'],propiedad=i['propiedad'],area=i['area'],tipo=i['tipo'],clase_tipo=i['clase_tipo'],modelo=i['modelo'],
                              ubicacion=i['ubicacion'],estado=i['estado'],fin_de_obra=find_de_obra_tmp,fase=i['fase'],bloqueo=i['bloqueo'],
                              precio=i['precio'],precio_sugerido=i['precio_sugerido'],proyecto_id=created_project,habitaciones=i['habitaciones'],
                              baños=i['baños'],parqueos=i['parqueos'],m2construccion=i['m2construccion'],
                              largo=i['largo'],ancho=i['ancho'],año=i['año'],titulo=i['titulo'],descripcion=i['descripcion'],detalles=i['detalles'],
                              descripcion_corta=i['descripcion_corta'],caracteristicas=i['caracteristicas'],latitud=i['latitud'],longitud=i['longitud'],
                              comision_referencia=i['comision_referencia'],comision_directa=i['comision_directa'],created_at=created_date_tmp,updated_at=updated_date_tmp,
                              api=True)

            new_property.save()
            property = new_property
        
        if 'imagenes' in i:
            exist_image = Images.objects.filter(property__external_id = i['id'])
            for j in i['imagenes']:
                if exist_image:
                    exist_image.update(property=property,tipo=j['tipo'],url=j['url'],api=True)
                else:
                    new_image = Images(property=property,tipo=j['tipo'],url=j['url'],api=True)
                    new_image.save()


class FilterPropiedad(TextFilter):
    title = _("Propiedad")
    parameter_name = "Propiedad"
    def queryset(self, request, queryset):
        if self.value() not in EMPTY_VALUES:
            # Here write custom query
            return queryset.filter(propiedad=self.value())

        return queryset

class FilterUbicacion(TextFilter):
    title = _("Ubicacion")
    parameter_name = "Ubicacion"
    def queryset(self, request, queryset):
        if self.value() not in EMPTY_VALUES:
            # Here write custom query
            return queryset.filter(ubicacion=self.value())

        return queryset
    

class FilterTipo(TextFilter):
    title = _("Tipo")
    parameter_name = "Tipo"
    def queryset(self, request, queryset):
        if self.value() not in EMPTY_VALUES:
            # Here write custom query
            return queryset.filter(tipo=self.value())

        return queryset




@admin.register(Property)
class CustomAdminClass(ModelAdmin):
    list_filter_submit = True 
    list_filter = [FilterPropiedad,FilterUbicacion,FilterTipo]


    def changelist_view(self, request, extra_context=None):
        get_data_from_api()
        exclude = ('api')
        # Aquí va tu lógica personalizada
        print(f"Usuario {request.user} ingresó al listado de MiModelo!!!")
        # También puedes actualizar modelos o hacer logging
        return super().changelist_view(request, extra_context=extra_context)
    
    pass

@admin.register(Proyect)
class CustomProyectClass(ModelAdmin):
    pass

@admin.register(Images)
class CustomImagesClass(ModelAdmin):
    pass
# Register your models here.
