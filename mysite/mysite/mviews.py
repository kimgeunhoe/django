from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import View

class UserCreateView(CreateView):
    template_name = 'registration/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('polls:index')

class SessionTestView(View):
    template_name = 'session.html'

    def get(self, request):
        request.session['session_variable'] = 'test'
        return render(request, self.template_name)