from .forms import colaboraForm
from django.shortcuts import render, redirect
from .models import Colaborador

# Create your views here.


def index(request):

    return render(request, 'index.html')


def verdatos(request):

    colaboradores = Colaborador.objects.all()

    return render(request, 'verdatos.html', {'colaboradores': colaboradores})


def form_colabora(request):

    if request.method == 'POST':

        colabora_form = colaboraForm(request.POST, request.FILES)

        if colabora_form.is_valid():

            colabora_form.save()

            return redirect('index')

    else:

        colabora_form = colaboraForm()

    return render(request, 'form_colabora.html', {'colabora_form': colabora_form})


def mod_colabora(request, id):

    colaborador = Colaborador.objects.get(rut=id)

    datos = {

        'form': colaboraForm(instance=colaborador)

    }

    if request.method == 'POST':

        formulario = colaboraForm(
            request.POST, request.FILES, instance=colaborador)

        if formulario.is_valid:

            colaborador.delete()

            formulario.save()

            return redirect('verdatos')

    return render(request, 'mod_colabora.html', datos)


def del_colabora(request, id):

    del_colabora = Colaborador.objects.get(rut=id)

    del_colabora.delete()

    return redirect('verdatos')
