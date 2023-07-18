from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin




class HomePage(TemplateView):
    template_name = 'home.html'
    
    def get(self, request):
        return render(request, self.template_name)

class SignUpView(TemplateView):
    template_name = 'signup.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        return render(request, self.template_name, {'form': form})


class CustomLoginView(LoginRequiredMixin, LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    # def get_success_url(self):
    #     if self.request.user.is_authenticated:
    #         return reverse_lazy('homepage')
    #     else:
    #         return super().get_success_url()
