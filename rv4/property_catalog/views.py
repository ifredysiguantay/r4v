from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Property,Images
from .forms import ComentarioForm



def list(request):
    properties = Property.objects.all()
    portrait_properties = Images.objects.all().order_by('property__id').distinct('property__id')
    property_id = request.GET.get('id')
    property = None
    comentario_form = None
    image_property = None 

    print(property_id)

    if property_id:
        property = get_object_or_404(Property,pk = property_id)
        image_property = Images.objects.get(property__id=property_id,tipo='ingreso')
        if request.method == 'POST':
            comentario_form = ComentarioForm(request.POST)
            if comentario_form.is_valid():
                comentario = comentario_form.save(commit=False)
                comentario.propiedad = property
                comentario.save()
                return redirect(f'/properties/list/?id={property.id}')

        else:
            comentario_form = ComentarioForm()
    return render(request,'catalog/list.html',{'property':property,'portrait_properties':portrait_properties,'comentario_form': comentario_form,'image_property':image_property})
# Create your views here.
