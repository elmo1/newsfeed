from urlparse import urlparse

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	category_name = models.CharField(max_length = 50)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return self.category_name

	class Meta:
		verbose_name_plural = "categories"

# class Comment(models.Model):
# 	comment = models.TextField()
# 	moderator = models.ForeignKey(User, related_name = 'moderated_comments')
# 	created_at = models.DateTimeField(auto_now_add = True)
# 	updated_at = models.DateTimeField(auto_now = True)

# 	def __unicode__(self):
# 		return self.comment

# 	class Meta:
# 		verbose_name_plural = "comments"


class Story(models.Model):
	title = models.CharField(max_length = 200)
	url = models.URLField()
	points = models.IntegerField(default = 1)
	moderator = models.ForeignKey(User, related_name = 'moderated_stories')
	category = models.ForeignKey(Category)
	#comments = models.ForeignKey(Comment)
	voters = models.ManyToManyField(User, related_name = 'liked_stories')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	@property 
	def domain(self):
		return urlparse(self.url).netloc

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural = "stories"
