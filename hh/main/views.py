from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.forms import Worker_Register
from main.models import Worker


# Create your views here.


def start_page(request):
    # request.user
    user = request.user
    print(user.is_staff)
    print(user.username)
    return render(request, 'main/start.html')


def workers_list(request):
    return render(request, 'main/workers_list.html', {"workers": Worker.objects.all()})


def register(request):
    if request.method == 'POST':
        form = Worker_Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workers_list')
    else:
        form = Worker_Register()

    return render(request, 'main/register.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'main/log_in.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('start_page')


class UserLogoutView(LogoutView):
    template_name = 'main/log_out.html'
    next_page = reverse_lazy('start_page')


class Create_User(CreateView):
    template_name = 'main/create_user.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('start_page')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('start_page')
        return super().get(request, *args, **kwargs)