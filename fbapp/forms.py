from .models import a,Profile,PhotoPost,Comment
from django import forms


class UserUpdate(forms.ModelForm):
    email=forms.CharField()
    class Meta:
        model=a
        fields=["first_name","last_name","email","username",]

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['profile_pic']


class PostImage(forms.ModelForm):
    class Meta:
        model=PhotoPost
        fields=["caption","photo"]


class PostComment(forms.Form):

    comment = forms.CharField()

#class PostComment(forms.ModelForm):


    class Meta:
        model=Comment
        fields=["comment"]
        #fields="__all__"
        widget={
            "comment":forms.TextInput(attrs={"placeholder":"Comment"})
        }







