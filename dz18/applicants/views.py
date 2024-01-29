from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from applicants.forms import CreateResumeForm
from applicants.models import Resume


# Create your views here.
class ResumeListView(ListView):
    model = Resume
    template_name = 'applicants/resume_list.html'
    context_object_name = 'resumes'

class ResumeDetailView(DetailView):
    model = Resume
    template_name = 'applicants/resume_detail.html'
    context_object_name = 'resume'

class ResumeCreateView(CreateView):
    model = Resume
    form_class = CreateResumeForm
    template_name = 'applicants/resume_create.html'
    context_object_name = 'form'
    success_url = reverse_lazy('resume_list')

class ResumeUpdateView(UpdateView):
    model = Resume
    form_class = CreateResumeForm
    template_name = 'applicants/resume_update.html'
    context_object_name = 'form'
    success_url = reverse_lazy('resume_list')

class ResumeDeleteView(DeleteView):
    model = Resume
    template_name = 'applicants/resume_delete.html'
    context_object_name = 'resume'
    success_url = reverse_lazy('resume_list')