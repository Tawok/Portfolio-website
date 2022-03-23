from django import forms
from .models import CustomUser, SocialNetwork, UserProfile, UserProjects

class CustomUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confrim Password', widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'birth_date', 'country', 'email_address', 'mobile', 'phone', 'image']

        widgets = {'birth_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'})}


class SocialNetworkForm(forms.ModelForm):
    class Meta:
        model = SocialNetwork
        fields = ['site_name', 'site_url']

class UserprojectsForm(forms.ModelForm):
    class Meta:
        model = UserProjects
        fields = ['title', 'description', 'project_url', 'project_file']
