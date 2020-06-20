from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *

class CaseListView(ListView):
	model = Case
	template_name="case/case_list.html"

class CaseDetailView(DetailView):
	model=Case
	template_name="case/case_detail.html"

class CaseCreateView(CreateView):
	# model=Case
	template_name="case/case_new.html"
	form_class = CaseForm
	success_message = '建立成功'
	success_url = reverse_lazy('home')

class CaseUpdateView(UpdateView):
	model=Case
	fields='__all__'
	template_name='case/case_edit.html'

class CaseDeleteView(DeleteView):
	model=Case
	template_name="case/case_delete.html"
	success_url=reverse_lazy('home')
	
def load_township(request):
    country_id = request.GET.get('country')
    township = Township.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'case/city_dropdown_list_options.html', {'township': township})

