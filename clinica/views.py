from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico, Consulta
from .forms import ConsultaForm

# Create your views here.
def listar_medicos(request):
    medicos = Medico.objects.all()

    return render(request, 'listar_medicos.html', {'medicos': medicos})

def criar_consulta(request):
    if request.method == "POST":
        consultaForm = ConsultaForm(request.post)

        if consultaForm.is_valid():
            consultaForm.save()

            return redirect("base")
    else:
        consultaForm = ConsultaForm()
    return render(request, 'form_consulta.html', {'consultaForm': consultaForm})

def detalhes_consulta(request, pk):
    consultas = Consulta.objects.get(pk=pk)    

    return render(request, 'base.html', {'consultas': consultas})   