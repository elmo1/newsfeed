from django import forms
from django.forms import ModelForm 
from stories.models import Story 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StoryForm(ModelForm):
	class Meta:
		model = Story 
		exclude = ('points', 'moderator', 'voters',)

# class CommentForm(ModelForm):
# 	class Meta:
# 		model = Comment
# 		exclude = ('moderator',)

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user