from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserForm, SocialNetworkForm, ProfileForm
from .models import UserProfile

# Create your views here.

class UserCreationView(CreateView):
    template_name = 'users/create_user.html'
    form_class = CustomUserForm
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UserProfileView(DetailView):
    template_name = 'users/user_profile.html'
    model = UserProfile

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class UpdateUserProfileView(UpdateView):
    template_name = 'users/update_profile.html'
    model = UserProfile
    form_class = ProfileForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('users:profile', kwargs={'pk': pk})    

class UserSocialSitesView(CreateView):
    template_name = 'users/user_network.html'
    form_class = SocialNetworkForm

    def from_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('users:profile', kwargs={'pk': pk})

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    
    def get_success_url(self):
        return reverse_lazy('home-page')

class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = reverse_lazy('users:login')
    
