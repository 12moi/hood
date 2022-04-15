
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, NeighbourHood, Business, Post
from cloudinary.models import CloudinaryField


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'neighbourhood')

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ('admin',)


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighbourhood')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')

# <p class="font-weight-bold ml-5 mt-3 pb-1">Or Register in with</p>
#                 <span>
#                 <a href="{% url 'social:begin' 'google-oauth2' %}"><button type="button" class="login-with-google-btn ml-5 mb-1" >Continue with Google</button></a>
#                 <a href="{% url 'social:begin' 'facebook' %}"><button class="loginBtn loginBtn--facebook ml-5 mb-1">Continue Facebook</button></a>
#                 </span>

