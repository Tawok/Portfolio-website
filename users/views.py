from audioop import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserForm, SocialNetworkForm, ProfileForm, UserprojectsForm
from .models import SocialNetwork, UserProfile, UserProjects

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    
    def get_success_url(self):
        return reverse_lazy('home-page')

class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = reverse_lazy('users:login')

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
        context = super().get_context_data(**kwargs)
        context['sites'] = SocialNetwork.objects.all().filter(user=self.request.user)
        context['projects'] = UserProjects.objects.all().filter(user=self.request.user)
        return context

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
    template_name = 'users/create_network.html'
    model = SocialNetwork
    form_class = SocialNetworkForm

    def form_valid(self, form):
        obj_form = form.save(commit=False)
        obj_form.user = self.request.user
        obj_form = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('users:profile', kwargs={'pk': pk})

class UserSocialSitesUpdateView(UpdateView):
    template_name = "users/update_network.html"
    model = SocialNetwork
    form_class = SocialNetworkForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('users:profile', kwargs={'pk': pk})

class UserSocialSitesDeleteView(DeleteView):
    template_name = "users/delete_network.html"
    model = SocialNetwork
    form_class = SocialNetworkForm
    context_object_name = 'site'

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('users:profile', kwargs={'pk': pk})

class UserProjectsView(CreateView):
    template_name = "users/add_project.html"
    model = UserProjects
    form_class = UserprojectsForm
    context_object_name = 'projects'

    def form_valid(self, form):
        obj_form = form.save(commit=False)
        obj_form.user = self.request.user
        obj_form = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('users:profile', kwargs={'pk': pk})

class UserProjectDetailView(DetailView):
    template_name = "users/projects_detail.html"
    model = UserProjects
    context_object_name = 'projects'

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('users:profile', kwargs={'pk': pk})

class UserProjectDeleteView(DeleteView):
    template_name = "users/projects_delete.html"
    model = UserProjects
    context_object_name = 'projects'

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('users:profile', kwargs={'pk': pk})

class UserProjectUpdateView(UpdateView):
    template_name = "users/projects_update.html"
    model = UserProjects
    form_class = UserprojectsForm
    context_object_name = 'projects'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('users:profile', kwargs={'pk': pk})


    
