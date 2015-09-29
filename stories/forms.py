#from django import forms
from django.forms import ModelForm 
from stories.models import Story 
#from stories.models import User
#from django.contrib.auth.forms import UserCreationForm

class StoryForm(ModelForm):
	class Meta:
		model = Story 
		exclude = ('points', 'moderator', 'voters',)

# class MyRegistrationForm(UserCreationForm):
# 	email = forms.EmailField(required = True)

# 	class Meta:
# 		model = User
# 		fields = ('username', 'email', 'password1', 'password2')

# 	def save(self, commit=True):
# 		user = super(MyRegistrationForm, self).save(commit=False)  
# 		user.email = self.cleaned_data['email']
# 		if commit: 
# 			user.save()

# 		return user 