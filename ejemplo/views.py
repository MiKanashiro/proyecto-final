from django.shortcuts import render
from ejemplo.models import Familiar, Mascota, Auto
from ejemplo.forms import Buscar, FamiliarForm, MascotaForm, AutoForm
from django.views import View


def index(request):
    return render(request, "ejemplo/saludar.html")

def saludar_a(request, nombre):
    
    return render(request, 
    "ejemplo/saludar_a.html", 
    {"nombre":nombre}
    )

def sumar(request, a, b):
    
    return render(request, 
    "ejemplo/sumar.html", 
    {"a": a, "b": b, "resultado": a+b}
    )

def buscar(request):

    query= request.GET["q"]
    lista_de_nombre = ["Juli","Coti","Cone"]

    if query in lista_de_nombre:
        indice= lista_de_nombre.index(query)
        resultado=lista_de_nombre[indice]
    else:
        resultado="no hay match"

    return render(request, "ejemplo/buscar.html", {"resultado": resultado})

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})


class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})


##############################################################################################################
def mostrar_mascotas(request):
  lista_mascotas = Mascota.objects.all()
  return render(request, "ejemplo/mascota.html", {"lista_mascotas": lista_mascotas})


class AltaMascota(View):

    form_class = MascotaForm
    template_name = 'ejemplo/alta_mascota.html'
    initial = {"nombre":"", "edad":"", "humano":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito la mascota {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

##############################################################################################################
def mostrar_autos(request):
  lista_autos = Auto.objects.all()
  return render(request, "ejemplo/auto.html", {"lista_autos": lista_autos})


class AltaAuto(View):

    form_class = AutoForm
    template_name = 'ejemplo/alta_auto.html'
    initial = {"modelo":"", "color":"", "patente":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el auto {form.cleaned_data.get('modelo')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})