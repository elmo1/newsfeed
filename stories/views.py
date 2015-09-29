import datetime

from django.contrib import auth
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext 
from django.utils.timezone import utc
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 
from django.core.context_processors import csrf

from stories.models import Story
from stories.models import Category 
from stories.forms import StoryForm 

def score(story, gravity=1.8, timebase=120):
    points = (story.points - 1)**0.8
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    age = int((now - story.created_at).total_seconds())/60

    return points/(age+timebase)**1.8

def top_stories(top=180, consider=1000):
    latest_stories = Story.objects.all().order_by('-created_at')[:consider]
    ranked_stories = sorted([(score(story), story) for story in latest_stories], reverse=True)
    return [story for _, story in ranked_stories][:top]


def index(request, category_id=1):
	stories = top_stories(top=30)
	category = Category.objects.get(id = category_id)
	if request.user.is_authenticated():
		liked_stories = request.user.liked_stories.filter(id__in = [story.id for story in stories])
	else: 
		liked_stories = []
	return render(request, 'stories/index.html', {
		'stories': stories,
		'user': request.user,
		'liked_stories': liked_stories,
		'category': category,
		})

@login_required(login_url = "/login/")
def story(request):
	if request.method == 'POST':
		form = StoryForm(request.POST)
		if form.is_valid():
			story = form.save(commit = False)
			story.moderator = request.user
			story.save()
			return HttpResponseRedirect('/')
	else:
		form = StoryForm()
	return render(request, 'stories/story.html', {'form': form})

@login_required
def vote(request):
	story = get_object_or_404(Story, pk = request.POST.get('story'))
	story.points += 1
	story.save()
	user = request.user
	user.liked_stories.add(story)
	user.save()
	return HttpResponse()

def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')

	args = {}
	args.update(csrf(request))

	args['form'] = UserCreationForm()

	return render_to_response('stories/register.html', args)


def category(request, category_name):
    template = 'stories/category.html'
    category = Category.objects.get(category_name = category_name)
    return render_to_response(template, {
        'category': category
        })
























