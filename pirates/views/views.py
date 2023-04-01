from django.shortcuts import render
from django.views import View
from ..models import Tesouro
from django.db.models import F, ExpressionWrapper, DecimalField, Sum
from .forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound


class ListaTesouro(View):
    def get(self, request):
        type_valor_total = DecimalField(max_digits=10, decimal_places=2)
        valor_total = ExpressionWrapper(F('preco') * F('quantidade'), output_field=type_valor_total)
        tesouros = Tesouro.objects.annotate(valor_total=valor_total)

        context = {'lista_tesouros': tesouros}
        context.update(tesouros.aggregate(total_geral=Sum('valor_total', output_field=type_valor_total)))

        return render(request, 'lista_tesouros.html', context)


class SalvarTesouro(View):
    def get(self, request, id=None):
        try:
            tesouro = Tesouro.objects.get(id=id)
        except Tesouro.DoesNotExist:
            tesouro = None

        return render(request, 'salvar_tesouro.html', {'form': SalvarTesouroForm(instance=tesouro)})

    def post(self, request, id=None):
        try:
            tesouro = Tesouro.objects.get(id=id)
        except Tesouro.DoesNotExist:
            tesouro = None

        form = SalvarTesouroForm(request.POST, request.FILES, instance=tesouro)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_tesouros'))

        return render(request, 'salvar_tesouro.html', {'form': form})


class RemoverTesouro(View):
    def get(self, request, id):
        try:
            Tesouro.objects.get(id=id).delete()
        except Tesouro.DoesNotExist:
            return HttpResponseNotFound()

        return HttpResponseRedirect(reverse('lista_tesouros'))
