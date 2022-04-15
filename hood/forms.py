
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



# <p class="font-weight-bold ml-5 mt-3 pb-1">Or Register in with</p>
#                 <span>
#                 <a href="{% url 'social:begin' 'google-oauth2' %}"><button type="button" class="login-with-google-btn ml-5 mb-1" >Continue with Google</button></a>
#                 <a href="{% url 'social:begin' 'facebook' %}"><button class="loginBtn loginBtn--facebook ml-5 mb-1">Continue Facebook</button></a>
#                 </span>

# .login-with-google-btn {
#     transition: background-color .3s, box-shadow .3s;
#     padding: 12px 16px 12px 42px;
#     border: none;
#     border-radius: 3px;
#     box-shadow: 0 -1px 0 rgba(0, 0, 0, .04), 0 1px 1px rgba(0, 0, 0, .25);
#     color: #757575;
#     font-size: 14px;
#     font-weight: 500;
#     font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen,Ubuntu,Cantarell,"Fira Sans","Droid Sans","Helvetica Neue",sans-serif;
    
#     background-image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj48cGF0aCBkPSJNMTcuNiA5LjJsLS4xLTEuOEg5djMuNGg0LjhDMTMuNiAxMiAxMyAxMyAxMiAxMy42djIuMmgzYTguOCA4LjggMCAwIDAgMi42LTYuNnoiIGZpbGw9IiM0Mjg1RjQiIGZpbGwtcnVsZT0ibm9uemVybyIvPjxwYXRoIGQ9Ik05IDE4YzIuNCAwIDQuNS0uOCA2LTIuMmwtMy0yLjJhNS40IDUuNCAwIDAgMS04LTIuOUgxVjEzYTkgOSAwIDAgMCA4IDV6IiBmaWxsPSIjMzRBODUzIiBmaWxsLXJ1bGU9Im5vbnplcm8iLz48cGF0aCBkPSJNNCAxMC43YTUuNCA1LjQgMCAwIDEgMC0zLjRWNUgxYTkgOSAwIDAgMCAwIDhsMy0yLjN6IiBmaWxsPSIjRkJCQzA1IiBmaWxsLXJ1bGU9Im5vbnplcm8iLz48cGF0aCBkPSJNOSAzLjZjMS4zIDAgMi41LjQgMy40IDEuM0wxNSAyLjNBOSA5IDAgMCAwIDEgNWwzIDIuNGE1LjQgNS40IDAgMCAxIDUtMy43eiIgZmlsbD0iI0VBNDMzNSIgZmlsbC1ydWxlPSJub256ZXJvIi8+PHBhdGggZD0iTTAgMGgxOHYxOEgweiIvPjwvZz48L3N2Zz4=);
#     background-color: white;
#     background-repeat: no-repeat;
#     background-position: 12px 11px;
# }

# .loginBtn--facebook {
#     padding-top: 5px;
#     padding-bottom: 7px;
#     background-color: #4C69BA;
#     background-image: linear-gradient(#4C69BA, #3B55A0);
#     text-shadow: 0 -1px 0 #354C8C;
# }
# .loginBtn--facebook:before {
#     border-right: #364e92 1px solid;
#     background: url('https://s3-us-west-2.amazonaws.com/s.cdpn.io/14082/icon_facebook.png') 6px 6px no-repeat;
# }
# .loginBtn--facebook:hover,
# .loginBtn--facebook:focus {
#     background-color: #5B7BD5;
#     background-image: linear-gradient(#5B7BD5, #4864B1);
# }
