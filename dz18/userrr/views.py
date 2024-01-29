from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.
def StartPage(request):
    return render(request, 'start_page.html')

class SignUpView(CreateView):
    template_name = 'regi/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('start')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('login')

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_staff = self.request.POST.get('is_staff', False) == 'on'
        user.save()
        return super().form_valid(form)

class LoginView(LoginView):
    template_name = 'regi/login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('vacancy_list')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('start')
        return super().get(request, *args, **kwargs)

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('start')
