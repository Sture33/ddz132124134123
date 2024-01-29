

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from applicants.models import Vacancy
from employers.forms import CreateVacancyForm


# Create your views here.
class VacancyListView(ListView):
    model = Vacancy
    template_name = 'employers/vacancy_list.html'
    context_object_name = 'vacancies'

class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'employers/vacancy_detail.html'
    context_object_name = 'vacancy'

class VacancyCreateView(CreateView):
    model = Vacancy
    template_name = 'employers/vacancy_create.html'
    form_class = CreateVacancyForm
    context_object_name = 'form'
    success_url = reverse_lazy('vacancy_list')

class VacancyUpdateView(UpdateView):
    model = Vacancy
    template_name = 'employers/vacancy_update.html'
    form_class = CreateVacancyForm
    context_object_name = 'form'
    success_url = reverse_lazy('vacancy_list')

class VacancyDeleteView(DeleteView):
    model = Vacancy
    template_name = 'employers/vacancy_delete.html'
    context_object_name = 'vacancy'
    success_url = reverse_lazy('vacancy_list')