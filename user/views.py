from django.shortcuts import render, redirect
from django.views import generic
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User

class RegisterView(generic.View):
    template_name = 'registration/register.html'
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(self.request, self.template_name, { 'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']

            if password == password2:
                if User.objects.filter( email=email ).exists():
                    messages.info(self.request, 'Email Already Used')
                    return redirect('register')
                elif User.objects.filter( username=username ).exists():
                    messages.info(self.request, 'Usernme Already Used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
            else:
                messages.info(self.request, 'Password not the same')
                return redirect('register')
            return redirect('home')
        return render(request, self.template_name)