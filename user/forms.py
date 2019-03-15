from django import forms
from .models import UserProfile


class ProfileForm(forms.Form):
    phone = forms.CharField(label='Phone No', max_length=50, required=False)
    first_name = forms.CharField(label='First Name', max_length=50, required=False)
    last_name = forms.CharField(label='Last Name', max_length=50, required=False)
    zip = forms.CharField(label='Zip Code', max_length=7, required=False)
    address = forms.CharField(label='Address', max_length=200, required=False)


class SignupForm(forms.Form):

    def signup(self, request, user):
        user_profile = UserProfile()
        user_profile.user = user
        user.save()
        user_profile.save()
