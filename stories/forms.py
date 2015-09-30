#from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm 
from stories.models import Story 
#from stories.models import Comment

class StoryForm(ModelForm):
	class Meta:
		model = Story 
		exclude = ('points', 'moderator', 'voters',)